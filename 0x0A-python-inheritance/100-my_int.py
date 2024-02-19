#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """
    A custom class derived from the built-in int class.

    Methods:
    - __new__(*args, **kwargs): Creates a new instance of MyInt.
    - __eq__(other): Customizes the equality comparison.
    - __ne__(other): Customizes the inequality comparison.
    """

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance of MyInt.

        Parameters:
        - *args: Variable positional arguments.
        - **kwargs: Variable keyword arguments.

        Returns:
        - MyInt: A new instance of MyInt.
        """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        Customizes the equality comparison.

        Parameters:
        - other: The object to compare with.

        Returns:
        - bool: True if not equal, False if equal.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Customizes the inequality comparison.

        Parameters:
        - other: The object to compare with.

        Returns:
        - bool: True if equal, False if not equal.
        """
        return int(self) == other
