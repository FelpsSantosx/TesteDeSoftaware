import unittest
from polindromo import Polindromo

class TestPolindromo(unittest.TestCase):
    def test_polindromo(self):
        self.assertFalse(Polindromo('amor').eh_polindromo())
        self.assertTrue(Polindromo('arara').eh_polindromo())        
        self.assertFalse(Polindromo('pyhton').eh_polindromo())
        self.assertTrue(Polindromo('radar').eh_polindromo())
        
if __name__ == '__main__':
    unittest.main()