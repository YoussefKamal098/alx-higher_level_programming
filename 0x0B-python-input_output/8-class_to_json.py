#!/usr/bin/python3
"""
This module provides utility functions for working with JSON files in Python.

Functions:
- class_to_json(obj): Convert a class instance to a JSON-compatible dictionary.
"""


def class_to_json(obj):
    """
    Converts a user-defined class instance to a JSON dictionary.

    Parameter:
        obj: An instance of a class with public attributes to serialize.

    Returns:
        A dictionary representing the JSON-serialized form of the
        class instance,
        including public attributes and their values.

    Raises:
        TypeError: If the input object is not an instance of a class.
    """
    return obj.__dict__
