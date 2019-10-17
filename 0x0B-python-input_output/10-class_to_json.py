#!/usr/bin/python3
"""returns dictionary description for JSON object"""


def class_to_json(obj):
    """returns dictionary description"""
    return obj.__dict__
