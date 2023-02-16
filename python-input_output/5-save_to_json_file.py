#!/usr/bin/python3
import json
"""Module to write an object to a text file"""


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file from 'my_obj'"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
