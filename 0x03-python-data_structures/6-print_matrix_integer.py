#!/usr/bin/python3
def print_matrix_integer(mtrx=[[]]):
    for x in range(len(mtrx)):
        for y in range(len(mtrx[x])):
            print("{:d}".format(mtrx[x][y]),
                  end=" " if y < len(mtrx[x]) - 1 else "")
        print()
