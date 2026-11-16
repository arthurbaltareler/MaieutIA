
import unittest
from unittest.mock import Mock

from core.submission import submeter_entrada


class TestSubmissao(unittest.TestCase):

    def setUp(self):
        self.motor = Mock()
        self.motor.responder.return_value = "Resposta simulada"

    def test_encaminha_entrada_integralmente(self):
        entrada = (
            "def soma(a, b):\n"
            "    resultado = a + b\n"
            "    return resultado"
        )

        resposta = submeter_entrada(self.motor, entrada)

        self.motor.responder.assert_called_once_with(entrada)
        self.assertEqual(resposta, "Resposta simulada")

    def test_preserva_quebras_de_linha(self):
        entrada = "linha 1\n    linha 2\nlinha 3"

        submeter_entrada(self.motor, entrada)

        self.motor.responder.assert_called_once_with(entrada)

    def test_rejeita_entrada_vazia(self):
        with self.assertRaises(ValueError):
            submeter_entrada(self.motor, "")

        self.motor.responder.assert_not_called()

    def test_rejeita_entrada_com_apenas_espacos(self):
        with self.assertRaises(ValueError):
            submeter_entrada(self.motor, "   \n   ")

        self.motor.responder.assert_not_called()

    def test_rejeita_entrada_nao_textual(self):
        with self.assertRaises(TypeError):
            submeter_entrada(self.motor, 123)

        self.motor.responder.assert_not_called()


if __name__ == "__main__":
    unittest.main()
