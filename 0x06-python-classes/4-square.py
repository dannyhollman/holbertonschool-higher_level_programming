#!/usr/bin/python3
"""creates class for making square"""


class Square:
    """class for square"""
    def __init__(self, size=0):
        """function for initializing square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """returns size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
