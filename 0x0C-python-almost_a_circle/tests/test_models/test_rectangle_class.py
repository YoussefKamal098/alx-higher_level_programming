#!/usr/bin/python3
"""
The provided Python module contains a set of unit tests designed for a
Rectangle class defined in a larger codebase. The tests cover various aspects
of the Rectangle class, such as instantiation, attribute validation
(width, height, x, y), attribute accessors and mutators, area calculation,
and the __str__ and display methods. The test cases are organized into
different classes, each focusing on specific aspects of the Rectangle class,
ensuring its proper functionality and robustness. These tests serve as a
comprehensive suite to verify the correctness and reliability of the Rectangle
class implementation.
"""
import io
import sys
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """
    Test cases for the instantiation of the Rectangle class.
    """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_invalid_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_invalid_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_id_incrementation(self):
        rectangle1 = Rectangle(10, 2)
        rectangle2 = Rectangle(2, 10)
        rectangle3 = Rectangle(2, 2, 4)
        rectangle4 = Rectangle(4, 4, 2)
        rectangle5 = Rectangle(1, 2, 3, 4)
        rectangle6 = Rectangle(4, 3, 2, 1)

        self.assertEqual(rectangle1.id, rectangle2.id - 1)
        self.assertEqual(rectangle3.id, rectangle4.id - 1)
        self.assertEqual(rectangle5.id, rectangle6.id - 1)

    def test_valid_args(self):
        rectangle = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual(7, rectangle.id, )

    def test_invalid_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_attributes(self):
        r = Rectangle(5, 5, 0, 0, 1)
        with self.assertRaises(AttributeError):
            print(r.__width)
        with self.assertRaises(AttributeError):
            print(r.__height)
        with self.assertRaises(AttributeError):
            print(r.__x)
        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_width_getter_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rectangle.width)
        rectangle.width = 10
        self.assertEqual(10, rectangle.width)

    def test_height_getter_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rectangle.height)
        rectangle.height = 10
        self.assertEqual(10, rectangle.height)

    def test_x_getter_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rectangle.x)
        rectangle.x = 10
        self.assertEqual(10, rectangle.x)

    def test_y_getter_setter(self):
        rectangle = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rectangle.y)
        rectangle.y = 10
        self.assertEqual(10, rectangle.y)


class TestRectangleWidthAttribute(unittest.TestCase):
    """
    Test cases for the width attribute of the Rectangle class.
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
                    Rectangle(value, 2)

    def test_invalid_value(self):
        values = [-1, 0]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "width must be > 0"):
                    Rectangle(value, 2)

    def test_valid_value(self):
        values = [1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            with self.subTest(value=value):
                self.assertEqual(Rectangle(value, 2).width, value)


class TestRectangleHeightAttribute(unittest.TestCase):
    """
    Test cases for the height attribute of the Rectangle class.
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
                                            "height must be an integer"):
                    Rectangle(2, value)

    def test_invalid_value(self):
        values = [0, -1, -2, -10, -50, -100, -200, -1000000]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "height must be > 0"):
                    Rectangle(2, value)

    def test_valid_value(self):
        values = [1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            with self.subTest(value=value):
                self.assertEqual(Rectangle(2, value).height, value)


class TestRectangleXAttribute(unittest.TestCase):
    """
    Test cases for the x attribute of the Rectangle class.
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
                    Rectangle(2, 2, value)

    def test_invalid_value(self):
        values = [-1, -2, -10, -50, -100, -200, -1000000]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                    Rectangle(2, 2, value)

    def test_valid_value(self):
        values = [0, 1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            with self.subTest(value=value):
                self.assertEqual(Rectangle(2, 2, value).x, value)


class TestRectangleYAttribute(unittest.TestCase):
    """
    Test cases for the y attribute of the Rectangle class.
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
                    Rectangle(2, 2, 2, value)

    def test_invalid_value(self):
        values = [-1, -2, -10, -50, -100, -200, -1000000]

        for value in values:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                    Rectangle(2, 2, 2, value)

    def test_valid_value(self):
        values = [0, 1, 2, 10, 50, 100, 200, 1000000]

        for value in values:
            with self.subTest(value=value):
                self.assertEqual(Rectangle(2, 2, 2, value).y, value)


class TestRectangleOrderOfInitialization(unittest.TestCase):
    """
    Test cases for the order of initialization attributes in Rectangle class.
    """

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangleAreaMethod(unittest.TestCase):
    """
    Test cases for the area() method of the Rectangle class.
    """

    def setUp(self):
        self.default_rectangle = Rectangle(2, 10, 1, 1, 1)

    def test_area_small(self):
        self.assertEqual(20, self.default_rectangle.area())

    def test_area_large(self):
        large_rectangle = Rectangle(999999999999999,
                                    999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001,
                         large_rectangle.area())

    def test_area_changed_attributes(self):
        self.default_rectangle.width = 7
        self.default_rectangle.height = 14
        self.assertEqual(98, self.default_rectangle.area())

    def test_area_one_arg(self):
        with self.assertRaises(TypeError):
            self.default_rectangle.area(1)


class TestRectangleStdout(unittest.TestCase):
    """
    Test cases for __str__ and display methods of the Rectangle class.
    """

    @staticmethod
    def capture_stdout(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def assert_str_output(self, r, expected_output):
        capture = TestRectangleStdout.capture_stdout(r, "print")
        self.assertEqual(expected_output, capture.getvalue())

    def assert_display_output(self, r, expected_output):
        capture = TestRectangleStdout.capture_stdout(r, "display")
        self.assertEqual(expected_output, capture.getvalue())

    # Test __str__ method
    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        self.assert_str_output(r, f"[Rectangle] ({r.id}) 0/0 - 4/6\n")

    def test_str_method_width_height_x(self):
        rectangle = Rectangle(5, 5, 1)
        self.assert_str_output(rectangle,
                               f"[Rectangle] ({rectangle.id}) 1/0 - 5/5\n")

    def test_str_method_width_height_x_y(self):
        rectangle = Rectangle(1, 8, 2, 4)
        self.assert_str_output(rectangle,
                               f"[Rectangle] ({rectangle.id}) 2/4 - 1/8\n")

    def test_str_method_width_height_x_y_id(self):
        rectangle = Rectangle(13, 21, 2, 4, 7)
        self.assert_str_output(rectangle, "[Rectangle] (7) 2/4 - 13/21\n")

    def test_str_method_changed_attributes(self):
        rectangle = Rectangle(7, 7, 0, 0, [4])
        rectangle.width = 15
        rectangle.height = 1
        rectangle.x = 8
        rectangle.y = 10
        self.assert_str_output(rectangle, "[Rectangle] ([4]) 8/10 - 15/1\n")

    def test_str_method_one_arg(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rectangle.__str__(1)

    # Test display method
    def test_display_width_height(self):
        rectangle = Rectangle(2, 3, 0, 0, 0)
        self.assert_display_output(rectangle, "##\n##\n##\n")

    def test_display_width_height_x(self):
        rectangle = Rectangle(3, 2, 1, 0, 1)
        self.assert_display_output(rectangle, " ###\n ###\n")

    def test_display_width_height_y(self):
        rectangle = Rectangle(4, 5, 0, 1, 0)
        display = "\n####\n####\n####\n####\n####\n"
        self.assert_display_output(rectangle, display)

    def test_display_width_height_x_y(self):
        rectangle = Rectangle(2, 4, 3, 2, 0)
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assert_display_output(rectangle, display)

    def test_display_one_arg(self):
        rectangle = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rectangle.display(1)


class TestRectangleUpdateMethodWithArgs(unittest.TestCase):
    """
    Test cases for the update method of the Rectangle class with arguments.
    """

    def setUp(self):
        self.initialValues = (10, 10, 10, 10, 10)

    def test_update_valid_args(self):
        valid_test_cases = [
            ((), "[Rectangle] (10) 10/10 - 10/10"),
            ((89,), "[Rectangle] (89) 10/10 - 10/10"),
            ((89, 2), "[Rectangle] (89) 10/10 - 2/10"),
            ((89, 2, 3), "[Rectangle] (89) 10/10 - 2/3"),
            ((89, 2, 3, 4), "[Rectangle] (89) 4/10 - 2/3"),
            ((89, 2, 3, 4, 5), "[Rectangle] (89) 4/5 - 2/3"),
            ((89, 2, 3, 4, 5, 6), "[Rectangle] (89) 4/5 - 2/3"),
            ((None,), "[Rectangle] (None) 10/10 - 10/10"),
            ((None, 4, 5, 2), "[Rectangle] (None) 2/10 - 4/5"),
            ((89, 2, 3, 4, 5, 6), "[Rectangle] (89) 4/5 - 2/3"),
        ]

        for args, expected_result in valid_test_cases:
            with self.subTest(args=args):
                rectangle = Rectangle(*self.initialValues)
                rectangle.update(*args)
                self.assertEqual(str(rectangle), expected_result)

    def test_update_invalid_args(self):
        invalid_test_cases = [
            ((89, "invalid"), TypeError, "width must be an integer"),
            ((89, 0), ValueError, "width must be > 0"),
            ((89, -5), ValueError, "width must be > 0"),
            ((89, 2, "invalid"), TypeError, "height must be an integer"),
            ((89, 1, 0), ValueError, "height must be > 0"),
            ((89, 1, -5), ValueError, "height must be > 0"),
            ((89, 2, 3, "invalid"), TypeError, "x must be an integer"),
            ((89, 1, 2, -6), ValueError, "x must be >= 0"),
            ((89, 2, 3, 4, "invalid"), TypeError, "y must be an integer"),
            ((89, 1, 2, 3, -6), ValueError, "y must be >= 0"),
            ((89, "invalid", "invalid"), TypeError,
             "width must be an integer"),
            ((89, "invalid", 1, "invalid"), TypeError,
             "width must be an integer"),
            ((89, "invalid", 1, 2, "invalid"), TypeError,
             "width must be an integer"),
            ((89, 1, "invalid", "invalid"), TypeError,
             "height must be an integer"),
            ((89, 1, "invalid", 1, "invalid"), TypeError,
             "height must be an integer"),
            ((89, 1, 2, "invalid", "invalid"), TypeError,
             "x must be an integer"),
            ((89, 1, 2, "invalid", "invalid"), TypeError,
             "x must be an integer"),
            ((89, 1, 2, 3, "invalid", "invalid"),
             TypeError, "y must be an integer"),
            ((89, 1, 2, 3, "invalid", "invalid"),
             TypeError, "y must be an integer"),
        ]

        for args, error_type, error_msg in invalid_test_cases:
            with self.subTest(args=args):
                rectangle = Rectangle(*self.initialValues)
                with self.assertRaisesRegex(error_type, error_msg):
                    rectangle.update(*args)


class TestRectangleUpdateMethodWithKwargs(unittest.TestCase):
    """
    Test cases for the update method of the Rectangle class with
    keyword arguments.
    """

    def setUp(self):
        self.initialValues = (10, 10, 10, 10, 10)

    def test_update_valid_kwargs(self):
        valid_test_cases = [
            ({"id": 1}, "[Rectangle] (1) 10/10 - 10/10"),
            ({"width": 2, "id": 1}, "[Rectangle] (1) 10/10 - 2/10"),
            ({"width": 2, "height": 3, "id": 89},
             "[Rectangle] (89) 10/10 - 2/3"),
            ({"id": 89, "x": 1, "height": 2, "y": 3, "width": 4},
             "[Rectangle] (89) 1/3 - 4/2"),
            ({"y": 5, "x": 8, "id": 99, "width": 1, "height": 2},
             "[Rectangle] (99) 8/5 - 1/2"),
            ({"id": None}, "[Rectangle] (None) 10/10 - 10/10"),
            ({"id": None, "height": 7, "y": 9},
             "[Rectangle] (None) 10/9 - 10/7"),
            ({"id": 89, "x": 1, "height": 2}, "[Rectangle] (89) 1/10 - 10/2"),
            ({"id": 89, "width": 2, "height": 4, "y": 6},
             "[Rectangle] (89) 10/6 - 2/4"),
            ({"a": 5, "b": 10}, "[Rectangle] (10) 10/10 - 10/10"),
            ({"height": 5, "id": 89, "a": 1, "b": 54, "x": 19, "y": 7},
             "[Rectangle] (89) 19/7 - 10/5"),
        ]

        for kwargs, expected_result in valid_test_cases:
            with self.subTest(kwargs=kwargs):
                r = Rectangle(*self.initialValues)
                r.update(**kwargs)
                self.assertEqual(str(r), expected_result)

    def test_update_invalid_kwargs(self):
        invalid_test_cases = [
            ({"width": "invalid"}, TypeError, "width must be an integer"),
            ({"width": 0}, ValueError, "width must be > 0"),
            ({"width": -5}, ValueError, "width must be > 0"),
            ({"height": "invalid"}, TypeError, "height must be an integer"),
            ({"height": 0}, ValueError, "height must be > 0"),
            ({"height": -5}, ValueError, "height must be > 0"),
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
                rectangle = Rectangle(*self.initialValues)
                with self.assertRaisesRegex(error_type, error_msg):
                    rectangle.update(**kwargs)


class TestRectangleToDictionaryMethod(unittest.TestCase):
    """
    Test cases for the to_dictionary() method of the Rectangle class.
    """

    def test_to_dictionary_output(self):
        rectangle = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, rectangle.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rectangle1 = Rectangle(10, 2, 1, 9, 5)
        rectangle2 = Rectangle(5, 9, 1, 2, 10)
        rectangle2.update(**rectangle1.to_dictionary())
        self.assertNotEqual(rectangle1, rectangle2)

    def test_to_dictionary_arg(self):
        rectangle = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rectangle.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
