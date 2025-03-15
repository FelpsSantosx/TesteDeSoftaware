import unittest
from divisao import divisao

class TestDivisao(unittest.TestCase):
    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5.0)
        self.assertEqual(divisao(10, 3), 3.3333333333333335)
        self.assertEqual(divisao(10, 5), 2.0)

if __name__ == '__main__':
    unittest.main()        