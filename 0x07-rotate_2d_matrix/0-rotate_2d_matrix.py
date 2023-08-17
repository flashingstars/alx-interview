#!/usr/bin/python3
"""2d matrix rotation
"""
def transpose_matrix(matrix, n):
    """
    Swapping the row and column elements 

    Args:
        matrix (_type_): _description_
    """
    
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """
    Reverses each row of the input matrix

    Args:
        matrix (_type_): _description_
    """
    
    
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """
    Calling the function

    Args:
        matrix (_type_): _description_
    """
    
    
    n = len(matrix)

    # transpose matrix
    transpose_matrix(matrix, n)

    # reverse matrix
    reverse_matrix(matrix)