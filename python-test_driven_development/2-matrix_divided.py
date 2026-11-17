#!/usr/bin/python3
"""Module 2-matrix_divided.

This module provides matrix_divided, a function that divides every
element of a matrix (a list of lists of numbers) by a number and returns
a new matrix with the results rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element of matrix divided by div.

    matrix must be a list of equally sized lists of integers or floats,
    div must be a non zero number, and every result is rounded to 2 decimals.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(error)
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(error)
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(error)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
