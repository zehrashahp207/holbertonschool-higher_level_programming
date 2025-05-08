#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int or float): Number to divide all elements by.

    Returns:
        list: New matrix with each value divided and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
