#!/usr/bin/python3
"""Class defines a student by certain parameters"""


class Student:
    """Class definition"""

    def __init__(self, first_name, last_name, age):
        """Initialization of constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that returns the __dict__ attributes of 'obj'"""
        return self.__dict__
