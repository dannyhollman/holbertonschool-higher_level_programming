#!/usr/bin/python3
"""reads n lines of a text file"""


def read_lines(filename="", nb_lines=0):
    """reads n lines"""
    lines = 0
    i = 0
    with open(filename) as f:
        data = f.read()

        for x in data:
            if x == '\n':
                lines += 1

        if nb_lines < 1:
            print(data)
            f.close()
            return
        new = data.split('\n')

        while i < lines and i < nb_lines:
            print(new[i])
            i += 1
        f.close()
