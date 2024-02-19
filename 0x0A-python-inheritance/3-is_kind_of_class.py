#!/usr/bin/python3
"""Module for is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or any of the classes in a tuple.

    Parameters:
    - obj: Any, the object to be checked.
    - a_class: Type or Tuple[Type], the class or tuple of classes for comparison.

    Returns:
    - bool: True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
