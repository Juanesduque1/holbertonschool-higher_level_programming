#!/usr/bin/python3
"""Module to create a function"""


def append_write(filename="", text=""):
    """Function to append text to text file"""
    with open(filename, 'a+', encoding="utf-8") as file:
        file.write(text)

    return len(text)
