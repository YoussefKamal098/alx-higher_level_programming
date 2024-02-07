#!/usr/bin/python3

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Example:
        To create a square with a size of 5:
        >>> square = Square(5)
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Example:
            To create a square with a size of 5:
            >>> square = Square(5)
        """
        self.__size = size
