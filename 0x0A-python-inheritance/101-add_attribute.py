#!/usr/bin/python3
"""Module for add_attribute function."""


def add_attribute(obj, att, value):
    """
    Dynamically adds an attribute to an object.

    Parameters:
    - obj: The object to which the attribute will be added.
    - att: The name of the attribute to be added.
    - value: The value of the attribute to be added.

    Raises:
    - TypeError: If the object does not support the addition of new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
