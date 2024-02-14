#!/usr/bin/python3
"""Unittest for max_integer function"""

import unittest

# Importing the max_integer function from the 6-max_integer module
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    """
    TestMaxIntegerFunction class

    A class containing unit tests for the max_integer function.
    """

    def test_ordered_list(self):
        """
        Test case for an ordered list.
        """
        ordered = [2, 4, 8, 16]
        self.assertEqual(max_integer(ordered), 16)

    def test_unordered_list(self):
        """
        Test case for an unordered list.
        """
        unordered = [8, 16, 2, 4]
        self.assertEqual(max_integer(unordered), 16)

    def test_max_at_beginning(self):
        """
        Test case for the maximum value at the beginning of the list.
        """
        max_at_beginning = [16, 2, 8, 4]
        self.assertEqual(max_integer(max_at_beginning), 16)

    def test_empty_list(self):
        """
        Test case for an empty list.
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """
        Test case for a list with only one element.
        """
        one_element = [16]
        self.assertEqual(max_integer(one_element), 16)

    def test_floats(self):
        """
        Test case for a list of floating-point numbers.
        """
        floats = [2.54, 7.43, -8.123, 15.25, 6.35]
        self.assertEqual(max_integer(floats), 15.25)

    def test_ints_and_floats(self):
        """
        Test case for a list containing both integers and
        floating-point numbers.
        """
        ints_and_floats = [2.54, 15.25, -8, 15, 7]
        self.assertEqual(max_integer(ints_and_floats), 15.25)

    def test_string(self):
        """
        Test case for a string input.
        """
        string = "Youssef"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """
        Test case for a list of strings.
        """
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """
        Test case for an empty string input.
        """
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
