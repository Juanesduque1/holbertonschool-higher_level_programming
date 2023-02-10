#!/usr/bin/python3
"""Function that adds two integers"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix = List of lists
        div = Number to divide all the elements of the matrix
    """

    """Data type validation"""
    if not all(list(map(lambda x: all(list(map(lambda num:
               isinstance(num, (int, float)), x))), matrix))):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    """Lenght of lists in list validation"""
    if not len(set(map(len, matrix))) == 1:
        raise TypeError("Each row of the matrix must have the same size")

    """Data type for div number validation"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """Div number greater than 0 validation"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """New matrix operation"""
    new_matrix = [[round(num / div, 2) for num in list] for list in matrix]
    return new_matrix
