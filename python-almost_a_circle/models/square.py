#!/usr/bin/python3
"""Class that inherits from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property to return size value"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter to size value and validations"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """str Built-in Method"""
        name = self.__class__.__name__
        size = self.width
        return f"[{name}] ({self.id}) {self.x}/{self.y} - {size}"

    def update(self, *args, **kwargs):
        """Public method to update attributes"""
        attr_list = ["id", "size", "x", "y"]
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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
