#!/usr/bin/python3
"""
This module provides utility functions for working with JSON in Python.

Functions:
- from_json_string(my_str): Convert the given JSON string to
  its corresponding Python object.

Parameters:
- my_str (str): The JSON string to be converted.

Returns:
- Any: The Python object represented by the input JSON string.

Note:
- This function uses the `json.loads` method from the `json` module
  to perform the conversion.
"""

import json


def from_json_string(my_str):
    """
    Convert the given JSON string to its corresponding Python object.

    Parameters:
    - my_str (str): The JSON string to be converted.

    Returns:
    - Any: The Python object represented by the input JSON string.

    Note:
    - This function uses the `json.loads` method from the `json` module
      to perform the conversion.
    """
    return json.loads(my_str)
