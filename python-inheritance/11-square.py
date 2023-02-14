#!/usr/bin/python3
"""Defining class to inherit"""

Rectangle = __import__('9-rectangle').Rectangle
"""Import for Rectangle class"""


class Square(Rectangle):
    """Class that inherits from Rectangle class"""

    def __init__(self, size):
        """Instantiation of new class"""
        self.__size = size

        """Usage of methods from Rectangle class"""
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)
