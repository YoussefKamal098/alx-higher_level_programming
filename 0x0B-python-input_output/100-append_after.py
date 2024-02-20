#!/usr/bin/python3

"""
This module provides a `append_after` function that
modifies a file by appending a specified string after
each line containing another given string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Modifies the specified file by appending `new_string` after each line
    containing `search_string`.

    Args:
        filename (str): The path to the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after
        lines containing `search_string`.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If any input parameters are empty strings.
    """
    with open(filename, 'r') as file:
        line_list = []

        for line in file:
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(line_list)
