#!/usr/bin/python3
"""Defining a class that contains a Square"""


class Square:
    """Class containing information about the square"""
    def __init__(self, size=0):
        """
        Initialization of object
        with size as private attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns area of the square
        """
        return self.__size ** 2
