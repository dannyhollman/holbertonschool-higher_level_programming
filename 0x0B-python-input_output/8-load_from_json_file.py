#!/usr/bin/python3
"""creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates object"""
    with open(filename) as f:
        data = f.read()
        j = json.loads(data)
        return j
