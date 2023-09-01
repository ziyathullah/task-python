import unittest
import pycalculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = pycalculator.add(5, 7)
        self.assertEqual(result, 12.0)

    def test_division_by_zero(self):
        result = pycalculator.divide(10, 0)
        self.assertEqual(result, "Cannot divide by zero")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            pycalculator.calculate("xyz", 5, 7)

if __name__ == '__main__':
    unittest.main()