#!/usr/bin/python3
"""Square module."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
        __position (int, int):  The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (int, int):  The position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.size * self.size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                not all(type(num) == int for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """ Prints a representation of the square using the '#' """
        if self.__size == 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print()

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()
