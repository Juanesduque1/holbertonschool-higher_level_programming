#!/usr/bin/python3
"""Module to create a function"""


def write_file(filename="", text=""):    
    """Function to read text and write to text file"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    
    return len(text)

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)