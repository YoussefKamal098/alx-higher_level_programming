#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A base class for geometry-related classes.

    Methods:
    - area(): Raises an exception indicating that it is not implemented.
    """

    def area(self):
        """
        Raise Exception: Indicates that the area() method is not implemented.
        """
        raise Exception('area() is not implemented')
