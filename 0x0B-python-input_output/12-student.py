#!/usr/bin/python3
"""create class Student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """convert to JSON"""
        final = {}
        dic = self.__dict__
        if attrs is not None:
            final = {k: v for (k, v) in dic.items() if k in attrs}
        else:
            final = {k: v for (k, v) in dic.items()}
        return final
