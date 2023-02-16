#!/usr/bin/python3
"""Pascal's triangle algorithm"""


def pascal_triangle(n):
    """Function that returns a list representing Pascal's triangle"""
    new_list = []

    """Size indicator n > 0 validation"""
    if n > 0:
        """Initialization of an empty list of lists with each position in 1"""
        new_list = [[1 for column in range(row)] for row in range(1, n + 1)]

        """Replacing of each list's elements according to Pascal's triangle"""
        for i in range(2, n):
            for j in range(1, i):
                new_list[i][j] = new_list[i - 1][j - 1] + new_list[i - 1][j]

    return new_list
