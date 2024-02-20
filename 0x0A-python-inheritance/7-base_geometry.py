#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """
    A base class for geometry-related classes.

    Methods:
    - area(): Raises an exception indicating that it is not implemented.
     - integer_validator(name, value): Validates that
     a given value is an integer greater than 0.
    """

    def area(self):
        """
        Raise Exception: Indicates that the area() method is not implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate that a given value is an integer greater than 0.

        Parameters:
        - name (str): The name of the value being validated.
        - value: The value to be validated.

        Raise:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
