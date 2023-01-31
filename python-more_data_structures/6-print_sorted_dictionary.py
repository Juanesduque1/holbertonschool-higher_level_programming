#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_by_key = sorted(a_dictionary)
    for key in sorted_by_key:
        print("{}: {}".format(key, a_dictionary[key]))
