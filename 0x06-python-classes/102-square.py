#!/usr/bin/python3
"""class for making square"""


class Square:
    """class for square"""
    def __init__(self, size=0):
        """initialize square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """get area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """return size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, other):
        """check if equal"""
        return self.size == other.size

    def __ne__(self, other):
        """check if not equal"""
        return self.size != other.size

    def __le__(self, other):
        """check if less than or equal"""
        return self.size <= other.size

    def __ge__(self, other):
        """check if greater than or equal"""
        return self.size >= other.size

    def __lt__(self, other):
        """check if less than"""
        return self.size < other.size

    def __gt__(self, other):
        """check if greater than"""
        return self.size > other.size
