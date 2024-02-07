#!/usr/bin/python3
"""Square module."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
