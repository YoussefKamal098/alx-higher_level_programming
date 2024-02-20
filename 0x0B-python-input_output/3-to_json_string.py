#!/usr/bin/python3
"""
This module provides utility functions for working with JSON in Python.

Functions:
- to_json_string(my_obj): Convert the given object to its JSON representation.

Parameters:
- my_obj: The Python object to be converted to JSON.

Returns:
- str: The JSON representation of the input object.

Note:
- This function uses the `json.dumps` method from the `json` module
  to perform the conversion.
"""

import json


def to_json_string(my_obj):
    """
    Convert the given object to its JSON representation.

    Parameters:
    - my_obj: The Python object to be converted to JSON.

    Returns:
    - str: The JSON representation of the input object.

    Note:
    - This function uses the `json.dumps` method from the `json` module
      to perform the conversion.
    """
    return json.dumps(my_obj)
