#!/usr/bin/python3
"""
The 'square' module, part of the 'models' package,
extends the functionalities provided by the 'Rectangle' module.
It introduces the 'Square' class, offering a structured representation
for square objects in Python applications. This class inherits from
the 'Rectangle' class and focuses on providing methods for updating,
converting to dictionaries, and obtaining parameters specific to squares.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class representing a square, inheriting from the Rectangle class.

    Attributes:
    - id (int): An identifier for the square.
    - x (int): x-coordinate of the top-left corner.
    - y (int): y-coordinate of the top-left corner.
    - size (int): Size of the square.
    """
    __slots__ = ("__size",)
    __params = {"size": 1}

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Parameter:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the top-left corner.
            Defaults to 0.
            y (int, optional): y-coordinate of the top-left corner.
            Defaults to 0.
            id (int, optional): Identifier for the square.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Property to get or set the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Args:
            value (int): New size value for the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if len(args) >= 2:
            args = list(args)
            insert_index, size = 1, args[1]
            args.insert(insert_index, size)

        if "size" in kwargs:
            kwargs["width"] = kwargs.pop("size")
            kwargs["height"] = kwargs["width"]

        super().update(*args, **kwargs)

    def to_dictionary(self):
        """
        Convert the square attributes to a dictionary.

        Returns:
            dict: Dictionary containing square attributes.
        """
        return {
            params: getattr(self, params) for params in Square.get_params()
        }

    @classmethod
    def get_params(cls):
        """
        Get the parameters of the Square class.

        Returns:
            tuple: Tuple containing the parameters of the Square class.
        """
        params = super().get_params() + tuple(cls.__params.keys())
        removed_params = ("width", "height")

        params = tuple(
            filter(lambda param: param not in removed_params, params)
        )

        return params

    @classmethod
    def get_params_with_default_values(cls):
        """
        Get the parameters with default values.

        Returns:
            MappingProxyType: Mapping proxy containing parameters and
            their default values.
        """
        params = dict(cls.__params)
        params.update(super().get_params_with_default_values())
        removed_params = ("width", "height")

        params = {key: value for key, value in params.items()
                  if key not in removed_params}

        return params

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: String representation of the square.
        """
        return f"[{type(self).__name__}] ({self.id}) " \
               f"{self.x}/{self.y} - {self.width}"
