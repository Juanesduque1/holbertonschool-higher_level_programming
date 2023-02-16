#!/usr/bin/python3
"""Function that returns an object mapped into a directory"""


def class_to_json(obj):
    """Return the __dict__ attributes of 'obj'"""
    return obj.__dict__
