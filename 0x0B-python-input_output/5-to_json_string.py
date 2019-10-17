#!/usr/bin/python3
"""returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """returns JSON"""
    j = json.dumps(my_obj)
    return j
