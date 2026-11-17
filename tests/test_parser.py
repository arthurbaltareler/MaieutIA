
import unittest

from core.parser import processar_entrada


class TestParser(unittest.TestCase):

    def test_preserva_indentacao_codigo(self):
        codigo = (
            "def soma(a, b):\n"
            "    resultado = a + b\n"
            "    return resultado"
        )

        self.assertEqual(processar_entrada(codigo), codigo)

    def test_normaliza_quebras_de_linha_windows(self):
        texto = "linha 1\r\nlinha 2\r\n    linha 3"

        esperado = "linha 1\nlinha 2\n    linha 3"

        self.assertEqual(processar_entrada(texto), esperado)

    def test_normaliza_quebras_de_linha_antigas(self):
        texto = "linha 1\rlinha 2"

        esperado = "linha 1\nlinha 2"

        self.assertEqual(processar_entrada(texto), esperado)

    def test_preserva_espacos_internos(self):
        texto = "  inicio\n    codigo\n  fim  "

        self.assertEqual(processar_entrada(texto), texto)

    def test_rejeita_entrada_vazia(self):
        with self.assertRaises(ValueError):
            processar_entrada("")

    def test_rejeita_entrada_com_apenas_espacos(self):
        with self.assertRaises(ValueError):
            processar_entrada("   \n   ")

    def test_rejeita_entrada_que_nao_seja_texto(self):
        with self.assertRaises(TypeError):
            processar_entrada(123)

    def test_rejeita_caractere_nulo(self):
        with self.assertRaises(ValueError):
            processar_entrada("codigo\0invalido")


if __name__ == "__main__":
    unittest.main()
