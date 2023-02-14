#!/usr/bin/python3
"""Function that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Module that returns True if is the same type, False otherwise"""
    if type(obj) is a_class:
        return True
    else:
        return False
