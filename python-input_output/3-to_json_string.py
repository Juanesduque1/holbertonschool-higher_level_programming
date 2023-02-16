#!/usr/bin/python3
"""Module return the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Function to return JSON representation of 'my_obj'"""
    return json.dumps(my_obj)
