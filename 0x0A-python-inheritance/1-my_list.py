#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """
    A custom list class derived from the built-in list class.

    This class inherits all the functionalities of the list class and
    adds a method to print the sorted version of the list.

    Attributes:
        No additional attributes.

    Methods:
        print_sorted(): Prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.
        """
        print(sorted(self))
