#!/usr/bin/python3
"""Module that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function create an object from a JSON file 'filename'"""
    with open(filename, 'r') as file:
        return json.load(file)
