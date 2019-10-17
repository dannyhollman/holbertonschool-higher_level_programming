#!/usr/bin/python3
"""reads and prints from text file"""


def read_file(filename=""):
    """opens and prints file"""
    with open(filename) as f:
        data = f.read()
        print(data)
        f.close()
