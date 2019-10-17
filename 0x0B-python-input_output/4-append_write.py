#!/usr/bin/python3
"""appends a string at the end of a file"""


def append_write(filename="", text=""):
    """appends to file"""
    with open(filename, "a") as f:
        count = f.write(text)
        f.close()
        return count
