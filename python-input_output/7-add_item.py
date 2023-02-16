#!/usr/bin/python3
"""Module to add all arguments to a Python list, then save them to a file"""
import sys
import json
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

arguments = sys.argv
filename = 'add_item.json'
list = []

"""Validating if file exists, if it does, save its content in a list"""
if os.path.exists(filename):
    list = load_from_json_file(filename)

"""Saving arguments in a Python list"""
for i in arguments[1:]:
    list.append(i)

"""Save list in the JSON file"""
save_to_json_file(list, filename)
