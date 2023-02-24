#!/usr/bin/python3
"""Class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property to return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to update width's value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property to return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to update height's value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property to return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter to update x's value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property to return y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter to update y's value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method to return area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Public method to display rectangle with character '#'"""
        string = ""
        if self.__height <= 0 or self.__width <= 0:
            return string

        print("{}".format("\n" * self.__y), end="")
        for i in range(0, self.__height):
            print("{}".format(" " * self.__x), end="")
            for j in range(0, self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        print()

    def __str__(self):
        """str Built-in Method"""
        name = self.__class__.__name__
        width = self.__width
        height = self.__height
        return f"[{name}] ({self.id}) {self.__x}/{self.__y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """Public method to update attributes"""
        attr_list = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr_list[i], args[i])
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Public method to return a dictionary repr of the class"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
