#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[i])):
            line.append(matrix[i][j] ** 2)
        new_matrix.append(line)
    return new_matrix
