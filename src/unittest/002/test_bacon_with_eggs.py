"""
TDD - Test Driven Development

RED
1 - Create tests and see it fail

GREEN
2 - Create code and see the test success

REFACTOR
3 - Improve code
"""

import unittest


class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs(0)
        print('test')

unittest.main(verbosity=2)
