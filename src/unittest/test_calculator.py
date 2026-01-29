from unittest import TestCase
import unittest
from calculator import sum_two
class TestCalculator(TestCase):
    def test_sum_5_5_return_10(self):
        self.assertEqual(sum_two(5,5), 10)


unittest.main(verbosity=2)