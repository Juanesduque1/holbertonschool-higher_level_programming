# Python - Almost a circle

Project done during my **Software Engineering studies** at **Holberton School**. It aims to learn skills in Python object-oriented programming by coding three connected classes to represent geometric figures as squares and rectangles. I wrote my own tests using the `unittest` module to test each class functionality.

The three classes coded in this project used the following Python tools:
* Imports
* Exceptions
* Public and private attributes
* Setter/getter methods
* Class/static methods
* Inheritance
* File I/O
* `args`/`kwargs` arguments
* JSON and CSV serialization/deserialization
* Unittesting

## Files
Files inside `models` folder:
| Filename | Description |
| -------- | ----------- |
| [`__init__.py`](./models/__init__.py) | Script that converts the `models` directory as a package. |
| [`base.py`](./models/base.py) | Base class of geometrical instances. |
| [`rectangle.py`](./models/rectangle.py) | Class that inherits attributes references from `Base` class. |
| [`square.py`](./models/square.py) | Class that inherits attributes references from `Square` class. |

Each class contains public/private attibutes, class/static methods and setters/getters. Also, some classes raise exceptions when is required (exeptions are commented for better understanding).

Files inside `tests/test_models` folder:

| Filename | Description |
| -------- | ----------- |
| [`__init__.py`](./tests/test_models/__init__.py) | Script that converts the `tests/test_models` directory as a package. |
| [`test_base.py`](./tests/test_models/test_base.py) | Test file that contains tests using `unittests` module for `Base` class. |
| [`test_rectangle.py`](./tests/test_models/test_rectangle.py) | Test file that contains `unittests` module for `Rectangle` class. |
| [`test_square.py`](./tests/test_models/test_square.py) | Test file that contains `unittests` module for `Square` class. |

## Authors

* Juan Esteban Duque <a href="https://github.com/Juanesduque1" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
