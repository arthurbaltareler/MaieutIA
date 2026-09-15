import os
from dotenv import load_dotenv
from openai import OpenAI


def main():

    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Erro: OPENAI_API_KEY não foi configurada.")
        return

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input="Explique em uma frase o que é um algoritmo."
    )

    print("Resposta da IA:")
    print(response.output_text)


if __name__ == "__main__":
    main()