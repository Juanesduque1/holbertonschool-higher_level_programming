#!/usr/bin/python3
"""Function that returns a list of attributes and methods of an object"""


def lookup(obj):
    """Return of the list with all the information about the object"""
    return dir(obj)
