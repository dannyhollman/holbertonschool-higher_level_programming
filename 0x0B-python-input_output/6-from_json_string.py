#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns JSON string"""
    j = json.loads(my_str)
    return j
