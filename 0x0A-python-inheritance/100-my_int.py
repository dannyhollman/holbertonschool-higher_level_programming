#!/usr/bin/python3
"""makes MyInt class"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """flips == with !="""
        return int(self) != other

    def __ne__(self, other):
        """flips == with !="""
        return int(self) == other
