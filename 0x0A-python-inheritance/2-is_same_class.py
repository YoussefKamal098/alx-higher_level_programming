#!/usr/bin/python3
"""Module for is_same_class method."""


def is_same_class(obj, a_class):
    """
    Check if the given object belongs to the specified class.

    Args:
        obj: Any - The object to check the class type.
        a_class: type - The class type to compare with.

    Returns:
        bool: True if the object belongs to the specified class
        False otherwise.
    """
    return type(obj) == a_class
