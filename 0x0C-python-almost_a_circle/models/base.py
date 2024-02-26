#!user/bin/python3
"""
The 'base' module, part of the 'models' package,
The Base module provides a foundation for managing objects with
common functionalities. It includes features for serializing
objects to JSON and CSV files, loading objects from these files,
and performing basic data validation. The module defines a Base class
with utility methods for working with objects in a consistent manner,
making it easier to handle data persistence and manipulation across
different classes.
"""
import csv
import json
import os
import turtle


class Base:
    """
    Base class for managing objects with common functionalities.

    Attributes:
    - id (int): An identifier for the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Parameters:
        - id (int, optional): An identifier for the object. If not provided,
          auto-increments the object counter to assign a unique ID.
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Parameters:
        - list_dictionaries (list): List of dictionaries to be converted.

        Returns:
        - str: JSON-formatted string.
        """
        list_dictionaries = list_dictionaries or []

        if type(list_dictionaries) is not list:
            raise TypeError("The first Argument must by a list")

        if not all(type(dictionary) is dict
                   for dictionary in list_dictionaries):
            raise TypeError("Every object in the list must be a dictionary")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Parameters:
        - list_objs (list): List of objects to be saved.
        """
        cls._check_save_to_file_args(list_objs)

        serialized_objs = [obj.to_dictionary() for obj in list_objs or []]

        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string(serialized_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Parameters:
        - json_string (str): JSON-formatted string.

        Returns:
        - list: List of dictionaries.
        """
        json_string = json_string or ""

        if type(json_string) is not str:
            raise ValueError("The first argument must be string json format")

        if not json_string:
            return []

        if Base._is_valid_json_format(json_string):
            return json.loads(json_string)
        else:
            raise ValueError("Invalid JSON format")

    def update(self, *args, **kwargs):
        """
        Update the object with new attributes.

        Parameters:
        - *args: Variable-length argument list.
        - **kwargs: Arbitrary keyword arguments.
        """
        pass

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class with the given dictionary
        of attributes.

        Parameters:
        - **dictionary: Arbitrary keyword arguments representing
        object attributes.

        Returns:
        - Base: A new instance of the class.
        """
        new_instance = cls(**cls.get_params_with_default_values())
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file.

        Returns:
        - list: List of objects loaded from the file.
        """
        file_path = f"{cls.__name__}.json"

        if not cls._is_readable_file(file_path):
            return []

        with open(file_path, "r") as file:
            list_dicts = cls.from_json_string(file.read())

            return [cls.create(**dictionary) for dictionary in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of objects to a CSV file.

        Parameters:
        - list_objs (list): List of objects to be saved.
        """
        file_path = f"{cls.__name__}.csv"

        cls._check_save_to_file_args(list_objs)

        with open(file_path, "w", newline="") as file:
            if not list_objs:
                file.write("[]")
                return

            first_obj = list_objs[0]

            writer = csv.DictWriter(file, fieldnames=first_obj.get_params())
            writer.writeheader()

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load objects from a CSV file.

        Returns:
        - list: List of objects loaded from the file.
        """
        file_path = f"{cls.__name__}.csv"

        if not cls._is_readable_file(file_path):
            return []

        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            cls._check_csv_file_required_fields(file_path, cls.get_params())

            list_dictionary = [{key: int(value) for key, value in row.items()}
                               for row in reader]

            return [cls.create(**dictionary) for dictionary in list_dictionary]

    @classmethod
    def _check_save_to_file_args(cls, list_objs):
        """
        Check the validity of arguments for save_to_file methods.

        Parameters:
        - list_objs (list): List of objects to be checked.
        """
        list_objs = list_objs or []

        if not isinstance(list_objs, list):
            raise TypeError("The first argument must be a list")

        if not all(isinstance(obj, cls) and type(obj) is not Base
                   for obj in list_objs):
            raise TypeError("Every object in the list must be a Child of Base")

        first_obj = list_objs[0] if len(list_objs) >= 1 else None

        if not all(type(obj) is first_obj.__class__ for obj in list_objs):
            raise TypeError("The list must contain the same class object type")

    @staticmethod
    def _check_integer(attribute_name, value, **kwargs):
        """
        Check if an attribute is an integer and satisfies a specified
        condition.

        Parameters:
        - attribute_name (str): Name of the attribute being checked.
        - value: Value of the attribute.
        - **kwargs: Additional keyword arguments for specifying comparison
        conditions.
        """
        compare_operators = {'>': '__gt__', '>=': '__ge__', '<': '__lt__',
                             '<=': '__le__', '==': '__eq__', '!=': '__ne__'}

        compare_op = kwargs.get('compare_op', '_eq__')
        compare_value = kwargs.get('compare_value', value)
        if type(value) is not int:
            raise TypeError(f"{attribute_name} must be an integer")
        if not isinstance(compare_value, int):
            raise TypeError("compare_value must be an integer")
        if compare_op not in compare_operators:
            raise TypeError("Invalid compare operator")
        if not getattr(value, compare_operators[compare_op])(compare_value):
            raise ValueError(f"{attribute_name} must be "
                             f"{compare_op} {compare_value}")

    @staticmethod
    def _is_readable_file(file_path):
        """
        Check if a file is readable.

        Parameters:
        - file_path (str): Path to the file.

        Returns:
        - bool: True if the file is readable, False otherwise.
        """
        if not os.path.exists(file_path):
            # print(f"Error: {file_path} does not exist.")
            return False

        if not os.path.isfile(file_path):
            # print(f"Error: {file_path} is a directory, not a file.")
            return False

        if not os.access(file_path, os.R_OK):
            # print(f"Error: {file_path} is not readable.")
            return False

        return True

    @staticmethod
    def _is_valid_json_format(json_string):
        """
        Check if a string is a valid JSON format.

        Parameters:
        - json_string (str): String to be checked.

        Returns:
        - bool: True if the string is a valid JSON format, False otherwise.
        """
        try:
            json.loads(json_string)
            return True
        except json.JSONDecodeError as error:
            print(f"JSON document: {error.doc}")
            print(f"Error position: {error.pos}")
            return False

    @staticmethod
    def _check_csv_file_required_fields(file_path, required_fields):
        """
        Check if a CSV file has the required fields.

        Parameters:
        - file_path (str): Path to the CSV file.
        - required_fields (tuple): Tuple of required field names.

        Raises:
        - IOError: If the file is not accessible.
        - TypeError: If the file is not a CSV file.
        - ValueError: If the CSV file is missing required fields.
        """
        if not Base._is_readable_file(file_path):
            raise IOError(f"can't access {file_path}")

        if not Base._is_csv_file(file_path):
            raise TypeError(f"The file {file_path} is not a csv file")

        with open(file_path, 'r', newline="") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames

            if not set(required_fields).issubset(header):
                raise ValueError(f"The CSV file is missing some "
                                 f"required fields. Expected: "
                                 f"{required_fields}, Found: {header}")

    @classmethod
    def _is_csv_file(cls, file_path):
        """
        Check if a file has a CSV extension.

        Parameters:
        - file_path (str): Path to the file.

        Returns:
        - bool: True if the file has a CSV extension, False otherwise.
        """
        if Base._get_file_extension(file_path) != ".csv":
            return False
        return True

    @staticmethod
    def _get_file_extension(file_path):
        """
        Get the extension of a file.

        Parameters:
        - file_path (str): Path to the file.

        Returns:
        - str: File extension.
        """
        return os.path.splitext(file_path)[1].lower()

    @classmethod
    def get_params(cls):
        """
        Get the parameter names of the class.

        Returns:
        - tuple: Tuple of parameter names.
        """
        return tuple("id", )

    @classmethod
    def get_params_with_default_values(cls):
        """
        Get the parameters with their default values as a mapping.

        Returns:
        - dict: Mapping of parameters to their default values.
        """
        return {"id": 0}

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.speed(2)
        turtle.pensize(5)
        turtle.bgcolor("white")

        for rectangle in list_rectangles + list_squares:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("orange")
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

        turtle.mainloop()
