#!/usr/bin/python3
"""
The provided Python module contains a set of unit tests designed for a
Square class defined in a larger codebase. The tests cover various aspects
of the Square class, such as instantiation, attribute validation
(size, x, y), attribute accessors and mutators, area calculation,
and the __str__ and display methods. The test cases are organized into
different classes, each focusing on specific aspects of the Square class,
ensuring its proper functionality and robustness. These tests serve as a
comprehensive suite to verify the correctness and reliability of the Square
class implementation.
"""
import io
import sys
import unittest

from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """
    Test cases for the instantiation of the Square class.
    """

    def test_is_base_and_rectangle(self):
        square = Square(10)
        self.assertIsInstance(square, Square)
        self.assertIsInstance(square, Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        square1 = Square(10)
        square2 = Square(11)
        self.assertEqual(square1.id, square2.id - 1)

    def test_size_and_id(self):
        square1 = Square(10, 2)
        square2 = Square(2, 10)
        self.assertEqual(square1.id, square2.id - 1)
        self.assertEqual(square1.size, 10)

    def test_size_and_position(self):
        square1 = Square(10, 2, 2)
        square2 = Square(2, 2, 10)
        self.assertEqual(square1.id, square2.id - 1)
        self.assertEqual(2, square1.x)
        self.assertEqual(2, square1.y)

    def test_size_position_and_id(self):
        square = Square(10, 2, 2, 7)
        self.assertEqual(7, square.id)
        self.assertEqual(10, square.size)
        self.assertEqual(2, square.x)
        self.assertEqual(2, square.y)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            Square(10, 2, 3, 4).__size

    def test_size_getter_and_setter(self):
        square = Square(4, 1, 9, 2)
        self.assertEqual(4, square.size)
        square.size = 8
        self.assertEqual(8, square.size)

    def test_width_and_height_getter(self):
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(8, square.width)
        self.assertEqual(8, square.height)

    def test_x_and_y_getter(self):
        self.assertEqual(0, Square(10).x)
        self.assertEqual(0, Square(10).y)


class TestSquareSizeAttribute(unittest.TestCase):
    """
    Test cases for the 'size' attribute of the Square class.
    """

    def test_invalid_type(self):
        values = [None, "str", 5.5, complex(5), {"a": 1, "b": 2},
                  True, [1, 2, 3], {1, 2, 3}, (1, 2, 3),
                  frozenset({1, 2, 3, 1}), range(5), b'Python',
                  bytearray(b'abcdefg'), memoryview(b'abcedfg'),
                  float('inf'), float('nan')]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError,
                                            "width must be an integer"):
                    Square(value)

    def test_invalid_value(self):
        values = [-1, 0]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "width must be > 0"):
                    Square(value)

    def test_valid_value(self):
        values = [1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            self.assertEqual(Square(value).size, value)


class TestSquareXAttribute(unittest.TestCase):
    """
    Test cases for the 'x' attribute of the Square class.
    """

    def test_invalid_type(self):
        values = [None, "str", 5.5, complex(5), {"a": 1, "b": 2},
                  True, [1, 2, 3], {1, 2, 3}, (1, 2, 3),
                  frozenset({1, 2, 3, 1}), range(5), b'Python',
                  bytearray(b'abcdefg'), memoryview(b'abcedfg'),
                  float('inf'), float('nan')]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "x must be an integer"):
                    Square(2, value)

    def test_invalid_value(self):
        values = [-1, -2, -10, -50, -100, -200, -1000000]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                    Square(2, value)

    def test_valid_value(self):
        values = [0, 1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            self.assertEqual(Square(2, value).x, value)


class TestSquareYAttribute(unittest.TestCase):
    """
    Test cases for the 'y' attribute of the Square class.
    """

    def test_invalid_type(self):
        values = [None, "str", 5.5, complex(5), {"a": 1, "b": 2},
                  True, [1, 2, 3], {1, 2, 3}, (1, 2, 3),
                  frozenset({1, 2, 3, 1}), range(5), b'Python',
                  bytearray(b'abcdefg'), memoryview(b'abcedfg'),
                  float('inf'), float('nan')]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "y must be an integer"):
                    Square(2, 2, value)

    def test_invalid_value(self):
        values = [-1, -2, -10, -50, -100, -200, -1000000]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                    Square(2, 2, value)

    def test_valid_value(self):
        values = [0, 1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            self.assertEqual(Square(2, 2, value).y, value)


class TestSquareOrderOfInitialization(unittest.TestCase):
    """
    Test cases for the order of initialization arguments in the Square class.
    """

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquareAreaMethod(unittest.TestCase):
    """
    Test cases for the 'area' method of the Square class.
    """

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        square = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, square.area())

    def test_area_changed_attributes(self):
        square = Square(2, 0, 0, 1)
        square.size = 7
        self.assertEqual(49, square.area())

    def test_area_one_arg(self):
        square = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            square.area(1)


class TestSquareStdout(unittest.TestCase):
    """
    Test cases for the standard output methods of the Square class.
    """

    @staticmethod
    def capture_stdout(sq, method):
        with io.StringIO() as capture:
            sys.stdout = capture
            if method == "print":
                print(sq)
            else:
                sq.display()
            sys.stdout = sys.__stdout__
            return capture.getvalue()

    def test_str_method_print_size(self):
        square = Square(4)
        expected_output = "[Square] ({}) 0/0 - 4\n".format(square.id)
        self.assertEqual(expected_output, self.capture_stdout(square, "print"))

    def test_str_method_size_x(self):
        square = Square(5, 5)
        expected_output = "[Square] ({}) 5/0 - 5".format(square.id)
        self.assertEqual(expected_output, square.__str__())

    def test_str_method_size_x_y(self):
        square = Square(7, 4, 22)
        expected_output = "[Square] ({}) 4/22 - 7".format(square.id)
        self.assertEqual(expected_output, str(square))

    def test_str_method_size_x_y_id(self):
        square = Square(2, 88, 4, 19)
        expected_output = "[Square] (19) 88/4 - 2"
        self.assertEqual(expected_output, str(square))

    def test_str_method_changed_attributes(self):
        square = Square(7, 0, 0, [4])
        square.size = 15
        square.x = 8
        square.y = 10
        expected_output = "[Square] ([4]) 8/10 - 15"
        self.assertEqual(expected_output, str(square))

    def test_str_method_one_arg(self):
        square = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            square.__str__(1)

    # Test display method
    def test_display_size(self):
        square = Square(2, 0, 0, 9)
        expected_output = "##\n##\n"
        self.assertEqual(expected_output,
                         self.capture_stdout(square, "display"))

    def test_display_size_x(self):
        square = Square(3, 1, 0, 18)
        expected_output = " ###\n ###\n ###\n"
        self.assertEqual(expected_output,
                         self.capture_stdout(square, "display"))

    def test_display_size_y(self):
        square = Square(4, 0, 1, 9)
        expected_output = "\n####\n####\n####\n####\n"
        self.assertEqual(expected_output,
                         self.capture_stdout(square, "display"))

    def test_display_size_x_y(self):
        square = Square(2, 3, 2, 1)
        expected_output = "\n\n   ##\n   ##\n"
        self.assertEqual(expected_output,
                         self.capture_stdout(square, "display"))

    def test_display_one_arg(self):
        square = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            square.display(1)


class TestRectangleUpdateMethodWithArgs(unittest.TestCase):
    """
    Test cases for the update method of the Rectangle class with arguments.
    """

    def setUp(self):
        self.initialValues = (10, 10, 10, 10)

    def test_update_valid_args(self):
        valid_test_cases = [
            ((), "[Square] (10) 10/10 - 10"),
            ((89,), "[Square] (89) 10/10 - 10"),
            ((89, 2), "[Square] (89) 10/10 - 2"),
            ((89, 2, 3), "[Square] (89) 3/10 - 2"),
            ((89, 2, 3, 4), "[Square] (89) 3/4 - 2"),
            ((89, 2, 3, 4, 5), "[Square] (89) 3/4 - 2"),
            ((89, 2, 3, 4, 5, 6), "[Square] (89) 3/4 - 2"),
            ((None,), "[Square] (None) 10/10 - 10"),
            ((None, 4, 5, 2), "[Square] (None) 5/2 - 4"),
            ((89, 2, 3, 4, 5, 6), "[Square] (89) 3/4 - 2"),
        ]

        for args, expected_result in valid_test_cases:
            with self.subTest(args=args):
                square = Square(*self.initialValues)
                square.update(*args)
                self.assertEqual(str(square), expected_result)

    def test_update_invalid_args(self):
        invalid_test_cases = [
            ((89, "invalid"), TypeError, "width must be an integer"),
            ((89, 0), ValueError, "width must be > 0"),
            ((89, -5), ValueError, "width must be > 0"),
            ((89, 2, "invalid"), TypeError, "x must be an integer"),
            ((89, 1, -5), ValueError, "x must be >= 0"),
            ((89, 2, "invalid"), TypeError, "x must be an integer"),
            ((89, 1, -6), ValueError, "x must be >= 0"),
            ((89, 2, 3, "invalid"), TypeError, "y must be an integer"),
            ((89, 1, 2, -6), ValueError, "y must be >= 0"),
            ((89, "invalid", "invalid"), TypeError,
             "width must be an integer"),
            ((89, "invalid", 1, "invalid"), TypeError,
             "width must be an integer"),
            ((89, "invalid", 1, 2), TypeError, "width must be an integer"),
            ((89, 1, "invalid", "invalid"), TypeError, "x must be an integer"),
            ((89, 1, 2, "invalid"), TypeError, "y must be an integer"),
        ]

        for args, error_type, error_msg in invalid_test_cases:
            with self.subTest(args=args):
                square = Square(*self.initialValues)
                with self.assertRaisesRegex(error_type, error_msg):
                    square.update(*args)


class TestRectangleUpdateMethodWithKwargs(unittest.TestCase):
    """
    Test cases for the update method of the Rectangle class with
    keyword arguments.
    """

    def setUp(self):
        self.initialValues = (10, 10, 10, 10)

    def test_update_valid_kwargs(self):
        valid_test_cases = [
            ({"id": 1}, "[Square] (1) 10/10 - 10"),
            ({"size": 2, "id": 1}, "[Square] (1) 10/10 - 2"),
            ({"width": 2, "size": 5, "id": 89}, "[Square] (89) 10/10 - 5"),
            ({"id": 89, "x": 1, "height": 2, "y": 3, "size": 4},
             "[Square] (89) 1/3 - 4"),
            ({"y": 5, "x": 8, "id": 99, "size": 20, "width": 1},
             "[Square] (99) 8/5 - 20"),
            ({"id": None}, "[Square] (None) 10/10 - 10"),
            ({"id": None, "size": 7, "y": 9}, "[Square] (None) 10/9 - 7"),
            ({"id": 89, "x": 1}, "[Square] (89) 1/10 - 10"),
            ({"id": 89, "size": 4, "y": 6}, "[Square] (89) 10/6 - 4"),
            ({"a": 5, "b": 10}, "[Square] (10) 10/10 - 10"),
            ({"size": 5, "id": 89, "a": 1, "b": 54, "x": 19, "y": 7},
             "[Square] (89) 19/7 - 5"),
        ]

        for kwargs, expected_result in valid_test_cases:
            with self.subTest(kwargs=kwargs):
                square = Square(*self.initialValues)
                square.update(**kwargs)
                self.assertEqual(str(square), expected_result)

    def test_update_invalid_kwargs(self):
        invalid_test_cases = [
            ({"width": "invalid"}, TypeError, "width must be an integer"),
            ({"size": 0}, ValueError, "width must be > 0"),
            ({"size": -5}, ValueError, "width must be > 0"),
            ({"size": "invalid"}, TypeError, "width must be an integer"),
            ({"size": 0}, ValueError, "width must be > 0"),
            ({"size": -5}, ValueError, "width must be > 0"),
            ({"x": "invalid"}, TypeError, "x must be an integer"),
            ({"x": -5}, ValueError, "x must be >= 0"),
            ({"y": "invalid"}, TypeError, "y must be an integer"),
            ({"y": -5}, ValueError, "y must be >= 0"),
            ({"id": 89, "width": 2, "height": "invalid"}, TypeError,
             "height must be an integer"),
            ({"id": 89, "width": 0}, ValueError, "width must be > 0"),
            ({"id": 89, "width": -5}, ValueError, "width must be > 0"),
            ({"id": 89, "x": "invalid"}, TypeError, "x must be an integer"),
            ({"id": 89, "x": -5}, ValueError, "x must be >= 0"),
            ({"id": 89, "y": "invalid"}, TypeError, "y must be an integer"),
            ({"id": 89, "y": -5}, ValueError, "y must be >= 0"),
        ]

        for kwargs, error_type, error_msg in invalid_test_cases:
            with self.subTest(kwargs=kwargs):
                square = Square(*self.initialValues)
                with self.assertRaisesRegex(error_type, error_msg):
                    square.update(**kwargs)


class TestSquareToDictionaryMethod(unittest.TestCase):
    """
    Test cases for the 'to_dictionary' method of the Square class.
    """

    def test_to_dictionary_output(self):
        square = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, square.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        square1 = Square(10, 2, 1, 2)
        square2 = Square(1, 2, 10)
        square2.update(**square1.to_dictionary())
        self.assertNotEqual(square1, square2)

    def test_to_dictionary_arg(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            square.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
