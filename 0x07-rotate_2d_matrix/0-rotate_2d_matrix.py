#!/usr/bin/python3
"""
Rotating a 2 x 2 matrix
"""


def rotate_2d_matrix(matrix):
    """rotates a matrix in a clockwise direction"""

    row_len = len(matrix)
    col_len = len(matrix[0])

    res = [[0] * row_len for n in range(len(matrix))]
    for i in range(col_len):
        for j in range(row_len):
            res[i][j] = matrix[j][i]
        res[i].reverse()

    for i in range(col_len):
        for j in range(row_len):
            matrix[i][j] = res[i][j]
