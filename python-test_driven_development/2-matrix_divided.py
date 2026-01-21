#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): Matrix to divide.
        div (int/float): Number to divide by.

    Returns:
        list of lists of floats: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   or if rows are not the same size, or div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Check div first to fail fast
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix
