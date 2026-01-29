import unittest
from unittest import TestCase

from calculator import sum_two


class TestCalculator(TestCase):
    def test_sum_5_5_return_10(self) -> None:
        self.assertEqual(sum_two(5, 5), 10)

    def test_minus_5_and_5_return_0(self) -> None:
        self.assertEqual(sum_two(-5, 5), 0)

    def test_various_entries(self) -> None:
        x_y_exits = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (1000, 1000, 2000),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, t_exit = x_y_exit
                self.assertEqual(sum_two(x, y), t_exit)

    def test_sum_x_is_not_int_or_float_must_return_assertionerror(self) -> None:
        with self.assertRaises(AssertionError):
            sum_two("a", 0)

    def test_sum_y_is_not_int_or_float_must_return_assertionerror(self) -> None:
        with self.assertRaises(AssertionError):
            sum_two(1, "0")


unittest.main(verbosity=2)
