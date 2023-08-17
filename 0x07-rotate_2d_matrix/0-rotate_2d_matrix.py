#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): The input n x n 2D matrix.

    Returns:
        None. The matrix is modified in-place.
    """


    n = len(matrix)

    #Transpose the matrix (Swap the rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
