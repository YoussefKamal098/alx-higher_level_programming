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

    def to_json(self):
        """
        Converts the Student object to a JSON dictionary.

        Returns:
            dict: A dictionary containing the student's
            attributes as key-value pairs.
        """
        return self.__dict__
