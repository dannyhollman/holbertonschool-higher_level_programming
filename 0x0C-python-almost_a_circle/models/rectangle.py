#!/usr/bin/python3
"""Rectangle class"""
from .base import Base
import json


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 1:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 1:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle"""
        for x in range(self.y):
            print()

        for x in range(self.height):
            for i in range(self.x):
                print(" ", end="")

            for y in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns rectangle in string format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        dic = {"x": self.x, "y": self.y, "id": self.id,
               "height": self.height, "width": self.width}
        return dic
