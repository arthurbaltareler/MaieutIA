import os
from datetime import datetime
from openai import OpenAI

# Carrega a chave da API
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Lê o System Prompt do projeto
with open("prompts/system_prompt_v1.md", "r", encoding="utf-8") as arquivo:
    system_prompt = arquivo.read()

# Cinco casos de teste
casos = [
    "Como verificar se um número é par ou ímpar?",
    "Como somar todos os números de 1 até N?",
    "Como encontrar o maior número de uma lista?",
    "Como funciona a busca binária?",
    "Meu código Python apresenta IndexError ao percorrer uma lista. Como corrigir?"
]

# Arquivo para registrar os resultados
with open("tests/resultados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Testes do Maieut-IA - {datetime.now()}\n\n")

    for i, pergunta in enumerate(casos, start=1):
        print(f"\nTeste {i}/5: {pergunta}")

        try:
            resposta = client.responses.create(
                model="gpt-4.1-mini",
                instructions=system_prompt,
                input=pergunta
            ).output_text

            print("Resposta:", resposta)

            arquivo.write(f"TESTE {i}\n")
            arquivo.write(f"Pergunta: {pergunta}\n")
            arquivo.write(f"Resposta: {resposta}\n")
            arquivo.write("-" * 50 + "\n")

        except Exception as erro:
            mensagem = f"Erro no teste: {erro}"
            print(mensagem)
            arquivo.write(f"TESTE {i}: {mensagem}\n")

print("\nTestes finalizados! Resultados salvos em tests/resultados.txt")