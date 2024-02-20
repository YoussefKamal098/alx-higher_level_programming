#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with the given attributes.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Initializes a Student object with the given attributes.

        Parameter:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except TypeError:
            return self.__dict__

        dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary

    def reload_from_json(self, json):
        """
        Updates the student's attributes with values from a JSON dictionary.

        Args:
            json (dict): A dictionary containing student
            attribute key-value pairs.

        Raises:
            ValueError: If the JSON dictionary contains invalid keys or values.
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
