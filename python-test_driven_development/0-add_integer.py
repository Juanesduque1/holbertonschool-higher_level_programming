#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """
    Args:
        a = int
        b = int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a, b = int(a),  int(b)
    return a + b
