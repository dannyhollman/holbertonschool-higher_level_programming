#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """funtion to divide all elements of a matrix"""
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers\
                        /floats")

    length = len(matrix[0])

    for x in matrix:
        if len(x) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                                integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    final = []
    for x in matrix:
        new = []
        for y in x:
            new.append(round(y / div, 2))
        final.append(new)

    return final
