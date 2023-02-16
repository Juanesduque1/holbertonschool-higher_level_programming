#!/usr/bin/python3
import json
"""Module to return data structure from a JSON string"""


def from_json_string(my_str):
    """Function to return data structure dict from 'my_str'"""
    return json.loads(my_str)
