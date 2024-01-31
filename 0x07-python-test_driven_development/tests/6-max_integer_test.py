#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([10, -3, 7, 0, -5]), 10)

if __name__ == '__main__':
    unittest.main()

