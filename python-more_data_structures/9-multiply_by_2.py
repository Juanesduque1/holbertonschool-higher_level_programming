#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdir = {}
    for i in a_dictionary:
        newdir[i] = a_dictionary[i] * 2
    return newdir
