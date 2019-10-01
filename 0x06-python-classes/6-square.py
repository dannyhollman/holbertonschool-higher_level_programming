#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()

        for x in range(self.position[1]):
            print()

        for i in range(self.__size):
            for x in range(self.position[1]):
                print(" " * self.position[0], end="")

            for j in range(self.__size):
                print("#", end="")

            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def check_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def check_position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(position) > 2 or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
