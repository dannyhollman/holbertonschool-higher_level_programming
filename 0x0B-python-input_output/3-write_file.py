#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """write to file"""
    with open(filename, "w") as f:
        count = f.write(text)
        f.close()
        return count
