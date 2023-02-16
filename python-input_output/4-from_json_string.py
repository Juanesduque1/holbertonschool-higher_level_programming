#!/usr/bin/python3
"""Module to return data structure from a JSON string"""
import json


def from_json_string(my_str):
    """Function to return data structure dict from 'my_str'"""
    return json.loads(my_str)
