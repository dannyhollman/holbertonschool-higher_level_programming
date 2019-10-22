#!/usr/bin/python3
"""Square class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns square in string format"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """updates attributes"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        dic = {"x": self.x, "y": self.y, "id": self.id, "size": self.height}
        return dic
