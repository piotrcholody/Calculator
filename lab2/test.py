import unittest
import sympy
from Calculator import Calculator
from unittest import TestCase
from unittest.mock import patch
import Exceptions


class Test(TestCase):

    def test_add(self):
        calc = Calculator()
        first = 21
        second = 37
        result = 58
        self.assertEqual(result, calc.add(first, second))

    def test_add_floats(self):
        calc = Calculator()
        first = 21.3
        second = 37.4
        result = 58.7
        self.assertAlmostEqual(result, calc.add(first, second))

    def test_add_exception_string(self):
        calc = Calculator()
        first = 21
        second = "asd"
        self.assertRaises(Exceptions.NotANumber, calc.add, first, second)

    def test_subtract(self):
        calc = Calculator()
        first = 21
        second = 37
        result = -16
        self.assertEqual(result, calc.subtract(first, second))

    def test_subtract_floats(self):
        calc = Calculator()
        first = 21.3
        second = 37.4
        result = -16.1
        self.assertAlmostEqual(result, calc.subtract(first, second))

    def test_subtract_exception_string(self):
        calc = Calculator()
        first = 21
        second = "asd"
        self.assertRaises(Exceptions.NotANumber, calc.subtract, first, second)

    def test_multiplicate(self):
        calc = Calculator()
        first = 10
        second = 5
        result = 50
        self.assertEqual(result, calc.multiplicate(first, second))

    def test_multiplicate_float(self):
        calc = Calculator()
        first = 12.5
        second = 2.5
        result = 31.25
        self.assertAlmostEqual(result, calc.multiplicate(first, second))

    def test_multiplicate_exception_string(self):
        calc = Calculator()
        first = 10
        second = "asd"
        self.assertRaises(Exceptions.NotANumber, calc.multiplicate, first, second)

    def test_divide(self):
        calc = Calculator()
        first = 10
        second = 5
        result = 2
        self.assertEqual(result, calc.divide(first, second))

    def test_divide_float(self):
        calc = Calculator()
        first = 12.5
        second = 2.5
        result = 5
        self.assertAlmostEqual(result, calc.divide(first, second))

    def test_divide_exception_string(self):
        calc = Calculator()
        first = 10
        second = "asd"
        self.assertRaises(Exceptions.NotANumber, calc.divide, first, second)

    def test_divide_exception_zero(self):
        calc = Calculator()
        first = 10
        second = 0
        self.assertRaises(Exceptions.DivideByZero, calc.divide, first, second)

    def test_logarithm(self):
        calc = Calculator()
        first = 8
        base = 2
        result = 3
        self.assertEqual(result, calc.logarithm(first, base))

    def test_logarithm_exception_base_one(self):
        calc = Calculator()
        first = 8
        base = 1
        self.assertRaises(Exceptions.NotValidLogarithmBase, calc.logarithm, first, base)

    def test_logarithm_base_exception_zero(self):
        calc = Calculator()
        first = 8
        base = 0
        self.assertRaises(Exceptions.NotValidLogarithmBase, calc.logarithm, first, base)

    def test_logarithm_exception_base_negative(self):
        calc = Calculator()
        first = 8
        base = -1
        self.assertRaises(Exceptions.NotValidLogarithmBase, calc.logarithm, first, base)

    def test_logarithm_exception_number_not_positive(self):
        calc = Calculator()
        first = -1
        base = 2
        self.assertRaises(Exceptions.NotAPositiveNumber, calc.logarithm, first, base)

    def test_logarithm_exception_number_zero(self):
        calc = Calculator()
        first = 0
        base = 2
        self.assertRaises(Exceptions.NotAPositiveNumber, calc.logarithm, first, base)

    @patch('sympy.diff', return_value='sin(x)')
    def test_derivative(self, mock_derivative):
        calc = Calculator()
        function = "sin(x)"
        variable = 2
        self.assertEqual(mock_derivative(function, 'x', variable), calc.derivative(function, variable))

if __name__ == "__main__":
    unittest.main()
