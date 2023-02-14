#!/usr/bin/python3
"""Module to create a function"""


def read_file(filename=""):
    """Function to read and write a text file"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
