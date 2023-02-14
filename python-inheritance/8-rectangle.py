#!/usr/bin/python3
"""Defining an empty class"""


class BaseGeometry:
    """Class containing information about basic geometry"""

    def area(self):
        """Public instance to raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate if an argument is an integer greater than 0"""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation of new class"""
        self.__width = width
        self.__height = height

        """Validation of data types"""
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
