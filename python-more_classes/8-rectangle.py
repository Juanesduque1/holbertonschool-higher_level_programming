#!/usr/bin/python3
"""Defining a class that contains a rectangle"""


class Rectangle:
    """Class containing information about the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Definition of constructor to instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Method to print the rectangle with built-in implementation"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                string += str(self.print_symbol)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """Method to return a string representation of the rectangle"""
        return "Rectangle(%i, %i)" % (self.width, self.height)

    def __del__(self):
        """Method to delete the object created"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to return the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
