#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a specific class
    and is a subclass of that class.

    Parameters:
    - obj: Any, the object to be checked.
    - a_class: Type, the class for comparison.

    Returns:
    - bool: True if obj is an instance and subclass of a_class,
    False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
