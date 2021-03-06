#!/usr/bin/python3
"""print square with #"""


def print_square(size):
    """print square"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(int(size)):
        for y in range(int(size)):
            print('#', end='')
        print()
