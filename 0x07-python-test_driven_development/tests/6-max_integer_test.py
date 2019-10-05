#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to test max_integer function"""
    def test_end(self):
        """test at end of list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_start(self):
        """test at start of list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_middle(self):
        """test in middle of list"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_same(self):
        """test all same input"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_two(self):
        """test with only two inputs"""
        self.assertEqual(max_integer([1, 9]), 9)

    def test_empty(self):
        """test with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """test with negative number"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
