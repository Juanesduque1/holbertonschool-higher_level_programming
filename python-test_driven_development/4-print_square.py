#!/usr/bin/python3
"""Function that prints a square based on its size"""


def print_square(size):
    """
    Args:
        size: Size of the square
    """

    """Size is an integer validation"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    """Size greater than 0 validation"""
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
