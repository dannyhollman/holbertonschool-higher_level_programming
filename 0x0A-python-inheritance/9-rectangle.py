#!/usr/bin/python3
"""makes BaseGeometry and Rectangle classes"""


class BaseGeometry:
    """BaseGeometry class"""
    def integer_validator(self, name, value):
        """checks if value is int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialize Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __repr__(self):
        """returns the rectangle in string format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
