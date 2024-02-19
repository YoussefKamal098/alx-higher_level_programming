#!/usr/bin/python3
"""Module for Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, derived from the BaseGeometry class.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(width, height): Initializes a Rectangle instance
    with specified width and height.
    - area(): Calculates and returns the area of the rectangle.
    - __str__(): Provides a human-readable string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with specified width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Note:
        - The width and height must be integers greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Provide a human-readable string representation of the rectangle.

        Returns:
        - str: A string representing the rectangle's dimensions.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
