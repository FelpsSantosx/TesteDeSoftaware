import unittest
from multiplicacao import multiplicacao

class testmultiplicacao(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(5, 3), 15)
        self.assertEqual(multiplicacao(10, 4), 40)
        self.assertEqual(multiplicacao(0, 5), 0)
        
if __name__ == '__main__':
    unittest.main() 