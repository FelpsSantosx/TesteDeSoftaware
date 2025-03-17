import unittest
from abrirArquivo import abrir_arquivo

class TestAbrirArquivo(unittest.TestCase):

    def test_arquivo_existe(self):
        self.assertTrue(abrir_arquivo("arquivo.txt"))

    def test_arquivo_nao_existe(self):
        self.assertFalse(abrir_arquivo("nao_existe.txt"))

if __name__ == '__main__':
    unittest.main()
