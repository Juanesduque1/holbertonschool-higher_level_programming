#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary
    delete_list = []
    for i in a_dictionary:
        delete_list = [k for k, v in a_dictionary.items() if v == value]

    for key in delete_list:
        new_dict.pop(key, a_dictionary)
    return new_dict
