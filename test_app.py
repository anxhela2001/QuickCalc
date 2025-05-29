"""
Author: Anxhela Halili
File: test_app.py
Purpose: This file contains unit tests for the `eval_expr` function defined in app.py.
         It ensures correct evaluation of a variety of mathematical expressions, 
         including edge cases.
Dependencies:
    - unittest (built-in)
    - app (local module)
"""

import unittest
from app import eval_expr

class TestMathEvaluator(unittest.TestCase):

    def test_addition_with_whitespace(self):
        self.assertEqual(eval_expr("  2    +   3 "), 5)

    def test_subtraction_with_whitespace(self):
        self.assertEqual(eval_expr("   10   -   4 "), 6)

    def test_multiplication_with_whitespace(self):
        self.assertEqual(eval_expr("  3   *    5 "), 15)

    def test_division_with_whitespace(self):
        self.assertEqual(eval_expr("  20   / 4   "), 5.0)

    def test_combined_operations(self):
        self.assertEqual(eval_expr(" 2 + 3 * 4 "), 14)

    def test_nested_parentheses(self):
        self.assertEqual(eval_expr(" (2 + 3) * (4 - 1) "), 15)

    def test_unary_minus(self):
        self.assertEqual(eval_expr(" -5 + 10 "), 5)

    def test_double_unary_minus(self):
        self.assertEqual(eval_expr(" -(-5) + 3 "), 8)

    def test_complex_expression(self):
        self.assertEqual(eval_expr(" 3 + 4 * 2 / (1 - 5) ** 2 "), 3 + 4 * 2 / (1 - 5)**2)

    def test_expression_with_floats(self):
        self.assertEqual(eval_expr(" 5.5 * 2 "), 11.0)

    def test_expression_with_float_division(self):
        self.assertEqual(eval_expr(" 7 / 2 "), 3.5)

    def test_expression_with_multiple_unaries(self):
        self.assertEqual(eval_expr(" -3 + -(-2) "), -1)

    def test_large_expression(self):
        self.assertEqual(eval_expr(" 1 + 2 + 3 * 4 - 5 / 2 + 6 * (2 + 3) "), 1 + 2 + 3 * 4 - 5 / 2 + 6 * (2 + 3))

    def test_exponentiation(self):
        self.assertEqual(eval_expr(" 2 ** 3 "), 8)

    def test_exponentiation_with_parentheses(self):
        self.assertEqual(eval_expr(" (2 + 1) ** 3 "), 27)

    def test_nested_expression_with_whitespace(self):
        self.assertEqual(eval_expr(" (  1 + 2  )  * (  3 + 4 ) "), 21)

    def test_whitespace_everywhere(self):
        self.assertEqual(eval_expr("   1   +   (   2   *   (  3  +   4 ) )   "), 15)

    def test_unary_and_exponent_combination(self):
        self.assertEqual(eval_expr(" -2 ** 2 "), -4)

    def test_long_whitespace_messy(self):
        self.assertEqual(eval_expr("   (   5 + 10   )   * (  2 - 3 +   4  ) "), (5 + 10) * (2 - 3 + 4))

    def test_no_spaces_at_all(self):
        self.assertEqual(eval_expr("3+4*2/(1-5)**2"), 3 + 4 * 2 / (1 - 5) ** 2)

    def test_decimal_with_spaces(self):
        self.assertEqual(eval_expr(" 3.14  *  2 "), 6.28)

