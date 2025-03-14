import unittest
from calculadora import soma, subtracao

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(10, 4), 6)
        self.assertEqual(subtracao(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
