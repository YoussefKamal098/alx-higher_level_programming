#!/usr/bin/python3
"""
This module provides a utility function for reading and printing the contents of a file in Python.

Functions:
- read_file(filename=""): Read and print the contents of a file.

Parameters:
- filename (str): The name of the file to be read. Default is an empty string.

Raises:
- FileNotFoundError: If the specified file is not found.
"""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Parameters:
    - filename (str): The name of the file to be read.
    Default is an empty string.
    """
    with open(filename, "r") as file:
        print(file.read(), end="")
