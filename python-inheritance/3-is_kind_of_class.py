#!/usr/bin/python3
"""Function that checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Module that returns True if is the same type, False otherwise"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
