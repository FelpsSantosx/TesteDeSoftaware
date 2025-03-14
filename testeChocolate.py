import unittest
from Chocolate import Chocolate  # Importa a classe do arquivo principal

class TestChocolate(unittest.TestCase):
    def test_criacao_chocolate(self):
        choco = Chocolate('branco')
        self.assertEqual(choco.sabor, 'branco')
        self.assertEqual(choco.get_preco(), 5)  # Testa o valor padrão

    def test_altera_preco(self):
        choco = Chocolate('amargo', 10)
        self.assertEqual(choco.get_preco(), 10)
        choco.altera_preco(15)
        self.assertEqual(choco.get_preco(), 15)

    def test_set_preco(self):
        choco = Chocolate('ao leite', 8)
        choco.set_preco(12)
        self.assertEqual(choco.get_preco(), 12)

if __name__ == '__main__':
    unittest.main()