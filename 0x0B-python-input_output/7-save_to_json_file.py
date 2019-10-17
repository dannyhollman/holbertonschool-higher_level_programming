#!/usr/bin/python3
"""writes an object to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """saves object to file"""
    with open(filename, "w") as f:
        j = json.dumps(my_obj)
        f.write(j)
        f.close()
