#!/usr/bin/python3
"""create class Student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialize Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """convert to JSON"""
        return self.__dict__
