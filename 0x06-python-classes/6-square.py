#!/usr/bin/python3
"""creates class for making square"""


class Square:
    """class for square"""
    def __init__(self, size=0, position=(0, 0)):
        """function for initializing square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")

                for j in range(self.__size):
                    print("#", end="")

                print()
