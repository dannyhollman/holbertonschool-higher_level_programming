#!/usr/bin/python3
def print_matrix_integer(mtrx=[[]]):
    column = len(mtrx)
    row = len(mtrx[0])
    for x in range(column):
        for y in range(row):
            print("{:d}".format(mtrx[x][y]), end=" " if y < column - 1 else "")
        print()
