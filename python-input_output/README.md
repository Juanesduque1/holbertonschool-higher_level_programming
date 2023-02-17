# Python - Input/Output

Project done during my **Software Engineering studies** at **Holberton School**. It aims to learn about file handling in **Python**. Also using the built-in `with`, `open`, and `read` functions with the `json` module to read and write files and serialize and deserialize objects with **JSON**.

## Files
| Filename | Description |
| -------- | ----------- |
| [`0-read_file.py`](./0-read_file.py) | Python function that prints the contents of a `UTF-8` text file to standard output. |
| [`1-write_file.py`](./1-write_file.py) | Python function that writes a string to a `UTF-8` text file and returns the number of characters written. |
| [`2-append_write.py`](./2-append_write.py) | Python function that appends a string to the end of a `UTF-8` text file and returns the number of characters appended. |
| [`3-to_json_string.py`](./3-to_json_string.py) | Python function that returns the `JSON` string representation of an object. |
| [`4-from_json_string.py`](./4-from_json_string.py) | Python function that returns the Python object represented by a `JSON` string. |
| [`5-save_to_json_file.py`](./5-save_to_json_file.py) | Python function that writes an object to a text file using `JSON` representation. |
| [`6-load_from_json_file.py`](./6-load_from_json_file.py) | Python function that creates an object from a `.json` file. |
| [`7-add_item.py`](./7-add_item.py) | Python script that stores all command line arguments to a Python list saved in the file `add_item.json`. |
| [`8-class_to_json.py`](./8-class_to_json.py) | Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers and booleans). |
| [`9-student.py`](./9-student.py) | Python class `Student` that defines a student with public instance attributes `first_name`, `last_name`, and `age`, instantiation with `first_name`, `last_name`, and `age`: `def __init__(self, first_name, last_name, age):` and public method `def to_json(self):` that returns the dictionary representation of a `Student` instance. |
| [`10-student.py`](./10-student.py) | Python class `Student` that defines a student with public method `def to_json(self, attrs=None):` that returns the dictionary representation of a `Student` instance, if `attrs` is a list of strings, only the attributes listed are represented in the dictionary. Builds on [`9-student.py`](./9-student.py). |
| [`11-student.py`](./11-student.py) | Python class `Student` that defines a student with public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance using the key/value pairs listed in `json`. Builds on [`10-student.py`](./10-student.py). |
| [`12-pascal_triangle.py`](./12-pascal_triangle.py) | Python function that returns a list of lists of integers representing Pascal's triangle of size `n`. |

## Authors

* Juan Esteban Duque <a href="https://github.com/Juanesduque1" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
