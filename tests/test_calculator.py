from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)
    
    def test_avg(self):
        self.assertEqual(self.calc.myavg(1, 2), 1.5)

    def test_max(self):
        self.assertEqual(self.calc.mymax(1, 2, 3), 3)
    
    
if __name__ == '__main__':
    unittest.main()