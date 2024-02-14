#!/usr/bin/python3
"""
    Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    Find and return the maximum value in a given list.

    Args:
    - lst (list or None): The input list.

    Returns:
    - int or float or None: The maximum value in the list. Returns None if the list is empty.
    """

    if type(list) is not list or len(list) == 0:
        return None

    return max(list)
