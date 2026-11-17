
import unittest
import httpx

from openai import (
    APIConnectionError,
    APITimeoutError,
    RateLimitError,
)

from core.errors import mensagem_fallback


class TestMensagemFallback(unittest.TestCase):

    def test_rate_limit(self):
        resposta = httpx.Response(
            429,
            request=httpx.Request(
                "POST",
                "https://api.openai.com/v1/chat/completions"
            )
        )

        erro = RateLimitError(
            message="Rate limit",
            response=resposta,
            body=None
        )

        mensagem = mensagem_fallback(erro)
        self.assertIn("temporariamente ocupado", mensagem)

    def test_timeout(self):
        erro = APITimeoutError(request=None)
        mensagem = mensagem_fallback(erro)
        self.assertIn("demorou para responder", mensagem)

    def test_erro_conexao(self):
        erro = APIConnectionError(request=None)
        mensagem = mensagem_fallback(erro)
        self.assertIn("Não foi possível conectar", mensagem)

    def test_erro_generico(self):
        erro = Exception("Erro desconhecido")
        mensagem = mensagem_fallback(erro)
        self.assertIn("Ocorreu um erro", mensagem)


if __name__ == "__main__":
    unittest.main()
