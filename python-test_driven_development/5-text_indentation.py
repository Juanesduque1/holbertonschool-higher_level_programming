#!/usr/bin/python3
"""Function that prints a text with certain conditions"""


def text_indentation(text):
    """
    Args:
        text: Text to modify
    """

    """Text is a string validation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    exceptions = [".", "?", ":"]
    counter = 0

    "Print text with new lines if i matches conditions"
    for i in range(len(text)):
        if i == len(text) - 1:
            print(text[counter:i + 1], sep="", end="")

        elif text[i] in exceptions:
            print(text[counter:i + 1], sep="")
            print()
            counter = i + 1

        "Do not print space after special character validation"
        while text[counter] == " ":
            counter = counter + 1
