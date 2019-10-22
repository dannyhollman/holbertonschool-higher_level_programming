#!/usr/bin/python3
"""unittest for Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """test Square class"""
    def test_sqr(self):
        """test square"""
        test = Square(10)
        self.assertEqual(test.size, 10)

    def test_sqr_size_type(self):
        """test width with wrong type"""
        test = Square(10)
        with self.assertRaises(TypeError):
            test.size = "10"

    def test_sqr_x_type(self):
        """test x with wrong type"""
        test = Square(10)
        with self.assertRaises(TypeError):
            test.x = "10"

    def test_sqr_y_type(self):
        """test y with wrong type"""
        test = Square(10)
        with self.assertRaises(TypeError):
            test.y = "10"

    def test_sqr_size_value(self):
        """test size with wrong value"""
        test = Square(10)
        with self.assertRaises(ValueError):
            test.width = 0

    def test_sqr_x_value(self):
        """test x with wrong value"""
        test = Square(10)
        with self.assertRaises(ValueError):
            test.x = -1

    def test_sqr_y_value(self):
        """test y with wrong value"""
        test = Square(10)
        with self.assertRaises(ValueError):
            test.y = -1

    def test_sqr_area(self):
        """test square area"""
        test = Square(10)
        self.assertEqual(test.area(), 100)

    def test_sqr_str(self):
        """test __str__"""
        test = Square(10, 1, 1, 1)
        self.assertEqual(str(test), "[Square] (1) 1/1 - 10")

    def test_sqr_update(self):
        """test update"""
        test = Square(10)
        test.update(size=1, x=1, y=1, id=1)
        self.assertEqual(str(test), "[Square] (1) 1/1 - 1")

    def test_sqr_to_dic(self):
        """test to_dictionary function"""
        test = Square(10, 1, 1, 1)
        new = test.to_dictionary()
        self.assertEqual(new, {'size': 10, 'x': 1, 'y': 1, 'id': 1})

