#!/usr/bin/python3
import json
"""Module return the JSON representation of an object"""


def to_json_string(my_obj):
    """Function to return JSON representation of 'my_obj'"""
    return json.dumps(my_obj)
