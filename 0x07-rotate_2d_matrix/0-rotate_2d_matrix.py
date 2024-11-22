#!/usr/bin/python3
"""
Rotating a 2 x 2 matrix
"""

def rotate_2d_matrix(matrix):
    """rotates a matrix in a clockwise direction"""

    row_len = len(matrix)
    col_len = len(matrix[0])

    res = [[0] * n for n in len(matrix)]
    for i in range(col_len):
        for j in range(row_len):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
        # matrix[i].reverse()
    # [[matrix[i][j] for j in range(col_len) for i in range(row_len)]]