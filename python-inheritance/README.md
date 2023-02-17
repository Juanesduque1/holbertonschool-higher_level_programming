# Python - Inheritance

Project done during my **Software Engineering studies** at **Holberton School**. It aims to learn about **Python's** class inheritance, the differences between super- and sub-classes, definining classes with multiple base classes, and overiding inherited methods and attributes.

## Files
| Filename | Description |
| -------- | ----------- |
| [`0-lookup.py`](./0-lookup.py) | Python function that returns a list of available attributes and methods of an object. |
| [`1-my_list.py`](./1-my_list.py) | Python class `MyList` that inherits from `list`. |
| [`2-is_same_class.py`](./2-is_same_class.py) | Python function that returns `True` if an object is exactly an instance of a specified class; otherwise `False`. |
| [`3-is_kind_of_class.py`](./3-is_kind_of_class.py) | Python function that returns `True` if an object is an instance or inherited instance of a specified class; otherwise `False`. |
| [`4-inherits_from.py`](./4-inherits_from.py) | Python function that returns `True` if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise `False`. |
| [`5-base_geometry.py`](./5-base_geometry.py) | An empty Python class `BaseGeometry`. |
| [`6-base_geometry.py`](./6-base_geometry.py) | Python class `BaseGeometry` with public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`. Builds on [`5-base_geometry.py`](./5-base_geometry.py). |
| [`7-base_geometry.py`](./7-base_geometry.py) | Python class `BaseGeometry` with public instance method `def integer_validator(self, name, value):` that validates the parameter `value`. Builds on [`6-base_geometry.py`](./6-base_geometry.py). |
| [`8-rectangle.py`](./8-rectangle.py) | Python class `Rectangle` that inherits from `BaseGeometry` ([`7-base_geometry.py`](./7-base_geometry.py)). |
| [`9-rectangle.py`](./9-rectangle.py) | Python class `Rectangle` with implementation of the method `area()` and special method `__str__` to print `Rectangle` in the format `[Rectangle] <width>/<height>`. Inherits from `BaseGeometry` ([`7-base_geometry.py`](./7-base_geometry.py)). Builds on [`8-rectangle.py`](./8-rectangle.py). |
| [`10-square.py`](./10-square.py) | Python class `Square` that inherits from `Rectangle` ([`9-rectangle.py`](./9-rectangle.py)) with private attribute `size` - validated with `integer_validator`, instantiation with `size`: `def __init__(self, size):` and implementation of the `area()` method. |
| [`11-square.py`](./11-square.py) | Python class `Square` that inherits from `Rectangle` ([`9-rectangle.py`](./9-rectangle.py)) with special method `__str__` to print `Square` in the format `[Square] <width>/<height>`. Builds on [`10-square.py`](./10-square.py). |

## Authors

* Juan Esteban Duque <a href="https://github.com/Juanesduque1" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>
