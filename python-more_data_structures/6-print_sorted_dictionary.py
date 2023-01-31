#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_by_key = dict(sorted(a_dictionary.items()))
    for key, value in sorted_by_key.items():
        print("{}: {}".format(key, value))
