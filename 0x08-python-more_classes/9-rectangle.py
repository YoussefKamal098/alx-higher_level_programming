#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    """int: The number of active instances."""

    print_symbol = "#"
    """type: Print symbol, can be any type."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """

        Rectangle.number_of_instances += 1

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        Note:
            If either the width or height is 0, the perimeter is considered 0.
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare the areas of two Rectangle instances and
        return the larger or equal one.

        Args:
            rect_1 (Rectangle): The first Rectangle instance.
            rect_2 (Rectangle): The second Rectangle instance.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an
            instance of Rectangle.

        Returns:
            Rectangle: The Rectangle instance with the greater or equal area.

        Note:
            If the areas are equal, rect_1 is returned.
    """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create and return a square instance of the Rectangle class.

        Args:
            size (int, optional): The size of the square (default is 0).

        Returns:
            Rectangle: A square instance with equal width and height.
        """
        return cls(size, size)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using '#' for each cell.

        Note:
            If either the width or height is 0, an empty string is returned.
        """

        if self.width == 0 or self.height == 0:
            return ""

        return "\n".join(
            [str(self.print_symbol) * self.width for _ in range(self.height)]
        )

    def __repr__(self):
        """
        Return a string representation of the rectangle for debugging.

        Returns:
            str: A string representing the rectangle with its width and height.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Destructor method for the Rectangle class.

        Prints a message when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
