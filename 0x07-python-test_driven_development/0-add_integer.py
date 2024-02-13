#!/usr/bin/python3
"""Module for add two integers"""


def add_integer(a, b=98):
    """
    Adds two integers.

    This function takes two arguments, 'a' and 'b',
    and returns their sum as an integer. If 'b' is not provided, it
    defaults to 98.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float.
        Defaults to 98.

    Returns:
        int: The sum of 'a' and 'b' converted to an integer.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
