#!/usr/bin/python3
"""Defining a class that contains a rectangle"""


class Rectangle:
    """Class containing information about the rectangle"""
    def __init__(self, width=0, height=0):
        """Definition of constructor to instantiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to get value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to get value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Method that returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)
