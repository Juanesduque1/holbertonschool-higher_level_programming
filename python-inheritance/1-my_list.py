#!/usr/bin/python3
"""Class that inherits from argument passed"""


class MyList(list):
    """Class that contains function to sort"""

    def print_sorted(self):
        """Function that sorts a list passed as argument"""
        new_list = self
        return print(sorted(new_list))
