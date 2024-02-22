#!user/bin/python3

"""
Module: base
----------------

The 'base' module contains the Base class, which represents a base object with an incremental identifier.
The class keeps track of the total number of objects created using the '__nb_objects' class variable.
The 'Base' class is designed to be inherited by other classes to provide a common base with automatic
identifier assignment.

Classes:
- Base: Represents a base object with an incremental identifier.
"""


class Base:
    """
    The Base class represents a base object with an incremental identifier.

    Attributes:
    - id (int): An identifier for the object.
    - __nb_objects (int): A class variable to keep track of the total number of objects created.

    Methods:
    - __init__(self, id=None): Initializes a new Base object. If an 'id' is provided, it is used as the identifier;
      otherwise, a unique identifier is generated.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base object.

        Parameters:
        - id (int, optional): An identifier for the object. If not provided, a unique identifier is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id += 1
