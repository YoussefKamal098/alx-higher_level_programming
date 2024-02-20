#!/usr/bin/python3
"""
This module provides utility functions for working with JSON in Python.

Functions:
- load_from_json_file(filename): Load a Python object from a JSON file.

Parameters:
- filename (str): The name of the JSON file from which the object
  will be loaded.

Returns:
- Any: The Python object loaded from the JSON file.

Note:
- This function uses the `json.load` method from the `json` module
  to read a Python object from the file.
"""

import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file from which the object will
      be loaded.

    Returns:
    - Any: The Python object loaded from the JSON file.

    Note:
    - This function uses the `json.load` method from the `json` module
      to read a Python object from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
