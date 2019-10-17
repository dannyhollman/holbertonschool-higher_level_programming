#!/usr/bin/python3
"""checks number of lines in file"""


def number_of_lines(filename=""):
    """counts lines in file"""
    lines = 0
    with open(filename) as f:
        data = f.read()
        for x in data:
            if x == '\n':
                lines += 1
        f.close()
        return lines
