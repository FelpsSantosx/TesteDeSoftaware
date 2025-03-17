import unittest
from pegarIdade import pegarIdade

class TestPegarIdade(unittest.TestCase):

    def test_pegar_idade(self):
        self.assertEqual(pegarIdade(10), 10)
        self.assertEqual(pegarIdade(-1), "Idade inválida")
        self.assertEqual(pegarIdade(0), "Idade inválida")
        self.assertEqual(pegarIdade("a"), "Idade inválida")

if __name__ == '__main__':
    unittest.main()
