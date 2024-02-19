#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

    def area(self):
        """
        Raise Exception: Indicates that the area() method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate that a given value is an integer greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
