#!/usr/bin/python3
"""
Docstring for python-test_driven_development.2-matrix_divided
matrix: list of lists of integers or floats
div: number (integer or float)
"""


def matrix_divided(matrix, div):
    """
    Docstring for matrix_divided
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix == []:
        raise ValueError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")

    return [[round(i / div, 2) for i in row] for row in matrix]
