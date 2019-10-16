#!/usr/bin/python3
"""checks if object is an instance or inherited from specified class"""


def is_kind_of_class(obj, a_class):
    """checks the object"""
    if isinstance(obj, a_class):
        return True
    return False
