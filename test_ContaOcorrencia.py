import unittest
from contaOcorrencia import ContaOcorrencia

class TestContaOcorrencia(unittest.TestCase):
    def test_contaOcorrencia(self):
        self.assertEqual(ContaOcorrencia('banana').contaOcorrencia(), {'b': 1, 'a': 3, 'n': 2})
        self.assertEqual(ContaOcorrencia('python').contaOcorrencia(), {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})
        self.assertEqual(ContaOcorrencia('paralelepipedo').contaOcorrencia(), {'p': 3, 'a': 2, 'r': 1, 'l': 2, 'e': 3, 'i': 1, 'd': 1, 'o': 1})
        self.assertEqual(ContaOcorrencia('').contaOcorrencia(), {})
        self.assertEqual(ContaOcorrencia('  ').contaOcorrencia(), {})
        self.assertEqual(ContaOcorrencia('chocolate com leite').contaOcorrencia(), {'a': 1, 'c': 3, 'e': 3, 'h': 1, 'i': 1, 'l': 2, 'm': 1, 'o': 3, 't': 2})

if __name__ == '__main__':
    unittest.main()
