#!/usr/bin/python3
"""Module for Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, derived from the Rectangle class.

    Attributes:
    - __size (int): The size of the square (side length).

    Methods:
    - __init__(size): Initializes a Square instance with a specified size.
    - area(): Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a specified size.

        Parameters:
        - size (int): The size of the square (side length).

        Note:
        - The size must be an integer greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size * self.__size
