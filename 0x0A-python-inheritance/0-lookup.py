#!/usr/bin/python3

def lookup(obj):
    """
    Provides a list of attributes and methods associated with the given object.

    Parameters:
    - obj: Any object
        The object for which attributes and methods are to be looked up.

    Returns: A list of strings containing the names of
    attributes and methods associated with the object.
    """
    return dir(obj)
