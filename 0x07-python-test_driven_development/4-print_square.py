#!/usr/bin/python3
"""Module for print square."""


def print_square(size):
    """
    Prints a square made of '#' characters with a specified size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
