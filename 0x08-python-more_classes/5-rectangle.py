#!/usr/bin/python3
"""creates rectanlge"""


class Rectangle:
    """class for rectangle"""
    def __init__(self, width=0, height=0):
        """init function"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """return heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            per = 0
        else:
            per = (self.__width * 2) + (self.__height * 2)
        return per

    def __str__(self):
        """returns string with rectangle"""
        final = ""
        if self.__height == 0 or self.__width == 0:
            return final
        for x in range(self.__height):
            for y in range(self.__width):
                final += '#'
            if x != self.__height - 1:
                final += '\n'
        return final

    def __repr__(self):
        """returns string representation of rectangle"""
        final = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return final

    def __del__(self):
        """print message when deleting"""
        print("Bye rectangle...")
