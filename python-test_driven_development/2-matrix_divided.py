#!/usr/bin/python3
"""
Module for dividing all elements of a matrix by a number.
matrix: list of lists of integers or floats
div: number (integer or float)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == []:
        raise ValueError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    for row in matrix:
        if row == matrix[0]:
            len_1 = len(row)
        len_2 = len(row)
        if len_1 != len_2:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for j in range(len(row)):
            if isinstance(row[j], (int, float)):
                new_row.append(round(row[j] / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        new_matrix.append(new_row)
    return new_matrix
