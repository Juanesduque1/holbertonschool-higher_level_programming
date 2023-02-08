#!/usr/bin/python3
"""Defining a class that contains a Square"""


class Square:
    """Class containing information about the square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of object
        with size as private attribute
        """
        self.size = size
        self.position = position

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

    """Instantiation of new method"""
    @property
    def position(self):
        """
        Returns position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Allows to see the position of the square
        """
        if len(value) != 2 or type(value) is not tuple or \
        not all(isinstance(i, int) and i >= 0 for i in value):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square
        """
        if self.size != 0:
            print("{}".format("\n" * self.__position[1]), end="")
            for i in range(self.__size):
                print("{}".format(" " * self.__position[0]), end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
