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
        """return area of square"""
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

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
