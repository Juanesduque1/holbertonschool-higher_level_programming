#!/usr/bin/python3
"""Defining an empty class"""


class BaseGeometry:
    """Class containing information about basic geometry"""
    def __init__(self):
        """Initialization of class"""
        pass

    def area(*args):
        """Public instance to raise an error"""
        raise Exception("area() is not implemented")
