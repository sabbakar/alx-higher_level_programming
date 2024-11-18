#!usr/bin/python3
"""
module of a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix.
    """
    if not matrix or not isinstance(matrix, list) or not all(\
            isinstance(row, list) for row in matrix):
        
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    if not (all(isinstance(row, list) for row in matrix) and
            all(all(isinstance(el, (int, float)) for el in row) for
                row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")

    # Get the length of the first row
    row_length = len(matrix[0])

    # Check if all rows have the same length
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
