
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


# Localiza a raiz do projeto
RAIZ = Path(__file__).resolve().parent.parent

# Carrega as variáveis do arquivo .env
load_dotenv(RAIZ / ".env")


class DialogueEngine:
    """Gerencia as chamadas à API e o histórico de uma conversa."""

    def __init__(self, prompt_path=None, model="gpt-4.1-mini"):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY não encontrada. Confira o arquivo .env."
            )

        if prompt_path is None:
            prompt_path = RAIZ / "prompts" / "system_prompt_v1.md"

        prompt_path = Path(prompt_path)

        with open(prompt_path, "r", encoding="utf-8") as arquivo:
            self.system_prompt = arquivo.read()

        self.client = OpenAI(api_key=api_key)
        self.model = model

        # O prompt permanece separado do histórico da conversa
        self.messages = []

    def responder(self, pergunta):
        """Envia uma mensagem e mantém o histórico entre os turnos."""

        pergunta = pergunta.strip()

        if not pergunta:
            raise ValueError("A mensagem não pode estar vazia.")

        # A mensagem do aluno entra no histórico
        self.messages.append({
            "role": "user",
            "content": pergunta
        })

        try:
            resposta = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    *self.messages
                ],
                temperature=0
            ).choices[0].message.content

            if not resposta:
                raise RuntimeError("A API retornou uma resposta vazia.")

            # Só registra a resposta depois de receber sucesso da API
            self.messages.append({
                "role": "assistant",
                "content": resposta
            })

            return resposta

        except Exception:
            # Remove a pergunta se a chamada falhar
            self.messages.pop()
            raise

    def limpar_historico(self):
        """Começa uma nova conversa sem perder o System Prompt."""
        self.messages.clear()
