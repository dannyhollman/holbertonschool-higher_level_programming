#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] ** 2)
        new.append(new_row)
    return new
