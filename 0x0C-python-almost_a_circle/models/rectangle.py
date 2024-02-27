#!/usr/bin/python3
"""
The 'rectangle' module, part of the 'models' package,
extends the functionalities provided by the 'Base' module.
It introduces the 'Rectangle' class, offering a structured
representation for rectangular objects in Python applications.
This module focuses on geometric entities and provides methods for
calculating area, displaying, updating attributes, and converting
to dictionaries.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with width, height, coordinates,
    and methods for area, display, updating attributes, and
    conversion to dictionaries.
    """
    __slots__ = ("__width", "__height", "__x", "__y")
    __args_with_default_values = {"id": None, "width": 1, "height": 1,
                                  "x": 0, "y": 0}

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the top-left corner.
            Defaults to 0.
            y (int, optional): y-coordinate of the top-left corner.
            Defaults to 0.
            id (int, optional): Identifier for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Property to get or set the width of the rectangle.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width property.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        Base._check_integer("width", value, compare_op='>', compare_value=0)
        self.__width = value

    @property
    def height(self):
        """
        Property to get or set the height of the rectangle.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        Base._check_integer("height", value, compare_op='>', compare_value=0)
        self.__height = value

    @property
    def x(self):
        """
        Property to get or set the x-coordinate of the rectangle.

        Returns:
            int: x-coordinate of the top-left corner.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x property.

        Args:
            value (int): New x-coordinate value.

        Raises:
            TypeError: If the x-coordinate is not an integer.
            ValueError: If the x-coordinate is less than 0.
        """
        Base._check_integer("x", value, compare_op='>=', compare_value=0)
        self.__x = value

    @property
    def y(self):
        """
        Property to get or set the y-coordinate of the rectangle.

        Returns:
            int: y-coordinate of the top-left corner.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y property.

        Args:
            value (int): New y-coordinate value.

        Raises:
            TypeError: If the y-coordinate is not an integer.
            ValueError: If the y-coordinate is less than 0.
        """
        Base._check_integer("y", value, compare_op='>=', compare_value=0)
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle on the console using '#' characters.
        """
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        rectangle_args = Rectangle.get_args()

        if args:
            for i, arg in enumerate(rectangle_args):
                setattr(self, arg,
                        args[i] if i < len(args) else getattr(self, arg))
        elif kwargs:
            for arg in rectangle_args:
                setattr(self, arg,
                        kwargs.get(arg, getattr(self, arg)))

    def to_dictionary(self):
        """
        Convert the rectangle attributes to a dictionary.

        Returns:
            dict: Dictionary containing rectangle attributes.
        """
        return {
            arg: getattr(self, arg) for arg in Rectangle.get_args()
        }

    @classmethod
    def get_args(cls):
        """
        Get the parameters of the Rectangle class.

        Returns:
            tuple: Tuple containing the parameters of the Rectangle class.
        """
        return tuple(cls.__args_with_default_values.keys())

    @classmethod
    def get_args_with_default_values(cls):
        """
        Get the parameters with default values.

        Returns:
            MappingProxyType: Mapping proxy containing parameters and
            their default values.
        """
        return dict(cls.__args_with_default_values)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return f"[{type(self).__name__}] ({self.id}) " \
               f"{self.x}/{self.y} - {self.width}/{self.height}"
