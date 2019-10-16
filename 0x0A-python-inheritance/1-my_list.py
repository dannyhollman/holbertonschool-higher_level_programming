#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """list class"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
