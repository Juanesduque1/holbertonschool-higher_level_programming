#!/usr/bin/python3
"""Defining Base class"""
import json
import os.path


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to return a JSON string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        """Static method to return a list of the JSON string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class to save the JSON string of 'list_objs'"""
        if list_objs is None:
            list_objs = []

        new_list = []
        for i in list_objs:
            new_list.append(i.to_dictionary())

        with open(f"{cls.__name__}.json", 'w') as file:
            file.write(Base.to_json_string(new_list))
    
    @classmethod
    def create(cls, **dictionary):
        """Class method to create an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)

        if cls.__name__ == "Square":
            obj = cls(1)
        
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Class method to return a list of instances"""
        filename = cls.__name__

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            data = Base.from_json_string(file.read())
        
        list = [cls.create(**dict) for dict in data]

        return list
