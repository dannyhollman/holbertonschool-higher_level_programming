#!/usr/bin/python3
"""adds new attribute to an object"""


def add_attribute(obj, attribute, value):
    """adds attribute to object"""
    try:
        obj.attribute = value
    except:
        raise TypeError("can't add new attribute")
