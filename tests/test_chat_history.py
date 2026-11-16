
import unittest

from core.chat_history import adicionar_mensagem


class TestHistoricoChat(unittest.TestCase):

    def test_adiciona_mensagem_do_aluno(self):
        historico = []

        adicionar_mensagem(historico, "user", "Minha dúvida")

        self.assertEqual(len(historico), 1)
        self.assertEqual(historico[0]["content"], "Minha dúvida")

    def test_adiciona_resposta_do_assistente(self):
        historico = []

        adicionar_mensagem(historico, "assistant", "Vamos começar.")

        self.assertEqual(historico[0]["role"], "assistant")

    def test_preserva_mensagens_anteriores(self):
        historico = []

        adicionar_mensagem(historico, "user", "Primeira pergunta")
        adicionar_mensagem(historico, "assistant", "Primeira dica")
        adicionar_mensagem(historico, "user", "Segunda pergunta")
        adicionar_mensagem(historico, "assistant", "Segunda dica")

        self.assertEqual(len(historico), 4)
        self.assertEqual(historico[0]["content"], "Primeira pergunta")
        self.assertEqual(historico[3]["content"], "Segunda dica")

    def test_rejeita_papel_invalido(self):
        with self.assertRaises(ValueError):
            adicionar_mensagem([], "system", "Mensagem")

    def test_rejeita_conteudo_nao_textual(self):
        with self.assertRaises(TypeError):
            adicionar_mensagem([], "user", 123)


if __name__ == "__main__":
    unittest.main()
