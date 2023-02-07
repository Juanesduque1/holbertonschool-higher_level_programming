#!/usr/bin/python3
"""Defining a class that contains a Square"""


class Square:
    """Class containing information about the square"""
    def __init__(self, size=0):
        """
        Initialization of object
        with size as private attribute
        """
        self.size = size

    @property
    def size(self):
        """
        Returns size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Allows to see the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square
        """
        if self.size is not 0:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
        else:
            print()
