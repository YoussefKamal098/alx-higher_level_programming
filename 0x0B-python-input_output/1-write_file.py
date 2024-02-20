#!/usr/bin/python3
"""
This module provides utility functions for reading files in Python.

Functions:
- write_file(filename="", text=""): Write the specified text to a file.

Parameters:
- filename (str): The name of the file to be written.
Default is an empty string.
- text (str): The text to be written to the file.
Default is an empty string.

Raises:
- FileNotFoundError: If the specified file is not found (for read_file).
"""


def write_file(filename="", text=""):
    """
    Write the specified text to a file.

    Parameters:
    - filename (str): The name of the file to be written.
    Default is an empty string.
    - text (str): The text to be written to the file.
    Default is an empty string.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, "w") as file:
        return file.write(text)
