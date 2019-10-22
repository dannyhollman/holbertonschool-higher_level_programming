#!/usr/bin/python3
"""unittest for Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class to test Rectangle"""
    def test_rec(self):
        """test rectangle class"""
        test = Rectangle(10, 2)
        self.assertEqual(test.width, 10)
        self.assertEqual(test.height, 2)

    def test_rec_id(self):
        """test rectangle id"""
        test = Rectangle(10, 2, 1, 1, 10)
        self.assertEqual(test.id, 10)

    def test_rec_area(self):
        """test rectangle area"""
        test = Rectangle(10, 2)
        self.assertEqual(test.area(), 20)

    def test_rec_set_width(self):
        """test setting width"""
        test = Rectangle(10, 2)
        test.width = 5
        self.assertEqual(test.width, 5)

    def test_rec_set_height(self):
        """test setting height"""
        test = Rectangle(10, 2)
        test.height = 5
        self.assertEqual(test.height, 5)

    def test_rec_set_x(self):
        """test setting x"""
        test = Rectangle(10, 2)
        test.x = 5
        self.assertEqual(test.x, 5)

    def test_rec_set_y(self):
        """test setting y"""
        test = Rectangle(10, 2)
        test.y = 5
        self.assertEqual(test.y, 5)

    def test_rec_width_type(self):
        """test width with wrong type"""
        test = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            test.width = "10"

    def test_rec_height_type(self):
        """test height with wrong type"""
        test = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            test.width = "2"

    def test_rec_x_type(self):
        """test x with wrong type"""
        test = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            test.x = "10"

    def test_rec_y_type(self):
        """test y with wrong type"""
        test = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            test.y = "10"

    def test_rec_width_value(self):
        """test width with wrong value"""
        test = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            test.width = 0

    def test_rec_height_value(self):
        """test height with wrong value"""
        test = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            test.height = 0

    def test_rec_x_value(self):
        """test x with wrong value"""
        test = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            test.x = -1

    def test_rec_y_value(self):
        """test y with wrong value"""
        test = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            test.y = -1

    def test_rec_to_dic(self):
        """test to_dictionary function"""
        test = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(test.to_dictionary(), {'width': 10, 'height': 2, 'x': 1, 'y': 1, 'id': 1})
