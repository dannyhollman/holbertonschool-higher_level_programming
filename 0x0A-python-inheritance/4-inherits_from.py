#!/usr/bin/python3
"""check if object is instance of class that inherited from specifed class"""


def inherits_from(obj, a_class):
    """checks object"""
    if issubclass(obj, a_class):
        return True
    return False
