#!/usr/bin/python3
"""Class defines a student by certain parameters"""


class Student:
    """Class definition"""

    def __init__(self, first_name, last_name, age):
        """Initialization of constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that returns the __dict__ attributes of 'obj'"""
        new_dict = {}

        if attrs is None:
            return self.__dict__

        for i in self.__dict__.keys():
            if i in attrs:
                new_dict[i] = self.__dict__[i]

        return new_dict

    def reload_from_json(self, json):
        """Public method to replace attributes of the Student instance"""
        for i in self.__dict__:
            self.__dict__[i] = json[i]
