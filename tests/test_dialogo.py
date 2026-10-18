
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Configure OPENAI_API_KEY no arquivo .env")

client = OpenAI(api_key=api_key)

# Localiza os arquivos a partir da raiz do projeto
raiz = Path(__file__).resolve().parent.parent
caminho_prompt = raiz / "prompts" / "system_prompt_v1.md"

with open(caminho_prompt, "r", encoding="utf-8") as arquivo:
    system_prompt = arquivo.read()

# Histórico da conversa
mensagens = [
    {
        "role": "system",
        "content": system_prompt
    }
]

# Simulação de uma conversa com vários turnos
perguntas = [
    "Como encontro o maior número de uma lista?",
    "Não sei por onde começar.",
    "Posso guardar o primeiro número como o maior?",
    "E como comparo os outros números?"
]

for numero, pergunta in enumerate(perguntas, start=1):
    print(f"\nAluno (turno {numero}): {pergunta}")

    mensagens.append({
        "role": "user",
        "content": pergunta
    })

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=mensagens,
        temperature=0
    ).choices[0].message.content

    print(f"Maieut-IA: {resposta}")

    mensagens.append({
        "role": "assistant",
        "content": resposta or ""
    })

print("\nSimulação de diálogo finalizada!")
