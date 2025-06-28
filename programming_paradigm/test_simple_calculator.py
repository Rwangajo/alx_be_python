# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, covering basic arithmetic
    operations and edge cases.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should be 0")
        self.assertEqual(self.calc.add(-1, -1), -2, "Should be -2")
        self.assertEqual(self.calc.add(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.add(100, 200), 300, "Should be 300")
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0, "Should handle floats")

    def test_subtraction(self):
        """
        Test the subtract method with various positive, negative, and zero inputs.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2, "Should be 2")
        self.assertEqual(self.calc.subtract(3, 5), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(1, -1), 2, "Should be 2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Should be 0")
        self.assertEqual(self.calc.subtract(10, 0), 10, "Subtracting zero should return same number")
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0, "Should handle floats")

    def test_multiplication(self):
        """
        Test the multiply method with various positive, negative, and zero inputs.
        Includes tests for multiplication by zero and one.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(-1, 5), -5, "Should be -5")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Should be 6")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Multiplying by zero should be 0")
        self.assertEqual(self.calc.multiply(5, 0), 0, "Multiplying by zero should be 0")
        self.assertEqual(self.calc.multiply(1, 10), 10, "Multiplying by one should return same number")
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0, "Should handle floats")

    def test_division(self): # Renamed from test_divide
        """
        Test the divide method, including normal division and the critical
        edge case of division by zero.
        """
        self.assertEqual(self.calc.divide(6, 3), 2.0, "Should be 2.0")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Should be 2.5")
        self.assertEqual(self.calc.divide(-10, 2), -5.0, "Should be -5.0")
        self.assertEqual(self.calc.divide(10, -2), -5.0, "Should be -5.0")
        self.assertEqual(self.calc.divide(-10, -2), 5.0, "Should be 5.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "Dividing zero by non-zero should be 0")
        self.assertIsNone(self.calc.divide(10, 0), "Dividing by zero should return None")
        self.assertIsNone(self.calc.divide(0, 0), "Dividing zero by zero should return None")
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0, "Should handle floats")


# This allows you to run the tests directly from the command line
# using 'python -m unittest test_simple_calculator.py'
if __name__ == '__main__':
    unittest.main()

