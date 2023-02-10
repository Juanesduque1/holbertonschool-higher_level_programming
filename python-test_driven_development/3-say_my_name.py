#!/usr/bin/python3
"""Function that prints first and last name of a person"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: First name of the person
        last_name: Last name of the person
    """

    """First name validation"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    """Last name validation"""
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
