#!/usr/bin/python3
"""Defining an empty class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Import for BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation of new class"""
        self.__width = width
        self.__height = height

        """Validation of data types"""
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
