#!/usr/bin/python3
"""unittest for Base"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """class to test Base class"""
    def test_pep8(self):
        """tests PEP8 format"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_set_id(self):
        """test setting id"""
        test = Base(10)
        self.assertEqual(test.id, 10)

    def test_create(self):
        """test create function"""
        test = Rectangle(1, 1, 1, 1, 1)
        test_dic = test.to_dictionary()
        test2 = Rectangle.create(**test_dic)
        self.assertEqual(str(test), str(test2))

