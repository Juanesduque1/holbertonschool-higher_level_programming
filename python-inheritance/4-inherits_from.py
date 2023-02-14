#!/usr/bin/python3
"""Function that checks if an object is an inheritance"""


def inherits_from(obj, a_class):
    """Module that returns True if is inheritance, False otherwise"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
