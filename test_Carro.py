import unittest
from carro import Carro

class TestCarro(unittest.TestCase):
    def test_acelerar(self):
        carro = Carro()
        self.assertEqual(carro.acelerar(), "Acelerando...")


if __name__ == '__main__':
    unittest.main()

