#!/usr/bin/python3
"""
This module provides utility functions for working with files in Python.

Functions:
- read_file(filename=""): Read and print the contents of a file.

Parameters:
- filename (str): The name of the file to be appended. Default is an empty string.
- text (str): The text to be appended to the file. Default is an empty string.

Raises:
- FileNotFoundError: If the specified file is not found for read_file.
"""


def append_write(filename="", text=""):
    """
    Append the specified text to a file.

    Parameters:
    - filename (str): The name of the file to be appended. Default is an empty string.
    - text (str): The text to be appended to the file. Default is an empty string.
    """
    with open(filename, "b") as file:
        return file.write(text)
