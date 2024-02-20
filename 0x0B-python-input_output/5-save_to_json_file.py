#!/usr/bin/python3
"""
This module provides utility functions for working with JSON in Python.

Functions:
- save_to_json_file(my_obj, filename): Save the given Python object to a
  JSON file.

Parameters:
- my_obj (Any): The Python object to be saved to the JSON file.
- filename (str): The name of the JSON file to which the object will be saved.

Note:
- This function uses the `json.dump` method from the `json` module
  to write the Python object to the file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save the given Python object to a JSON file.

    Parameters:
    - my_obj (Any): The Python object to be saved to the JSON file.
    - filename (str): The name of the JSON file to which the object
      will be saved.

    Note:
    - This function uses the `json.dump` method from the `json` module
      to write the Python object to the file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
