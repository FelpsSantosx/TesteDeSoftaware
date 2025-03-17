import unittest
from eh_primo import eh_primo

class TestEhPrimo(unittest.TestCase):
    def test_eh_primo(self):
        self.assertTrue(eh_primo(2))
        self.assertTrue(eh_primo(3))
        self.assertTrue(eh_primo(5))
        self.assertTrue(eh_primo(7))
        self.assertTrue(eh_primo(11))
        self.assertFalse(eh_primo(1))
        self.assertFalse(eh_primo(4))
        self.assertFalse(eh_primo(6))
        self.assertFalse(eh_primo(8))
        
if __name__ == '__main__':
    unittest.main()