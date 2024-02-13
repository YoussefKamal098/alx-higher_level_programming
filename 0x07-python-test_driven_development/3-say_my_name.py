#!/usr/bin/python3
"""Module for print first_name and last_name."""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).
    Raises:
        TypeError: If `first_name` is not a string.
        TypeError: If `last_name` is not a string.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/3-say_my_name.txt")
