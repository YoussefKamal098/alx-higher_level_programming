"""
Test module for unit testing the functionality of the
Base, Rectangle, and Square classes in a Python application.
This module contains a comprehensive set of test cases that cover
various aspects of instantiation, method behaviors, and file I/O operations
for the Base class, as well as its derived classes Rectangle and Square.
The tests ensure the correct implementation of methods like to_json_string,
save_to_file, from_json_string, create, load_from_file, save_to_file_csv,
and load_from_file_csv. The test cases are designed to verify the proper
functioning of the classes and their methods, as well as to maintain
code integrity across different scenarios. Each test class focuses on a
specific set of functionalities, providing clear and organized validation
for the implemented features of the application.
"""
import json
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """
    Test cases for the instantiation of the Base class.
    """

    def test_no_arg(self):
        base1, base2 = Base(), Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1, base2, base3 = Base(), Base(), Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None_id(self):
        base1, base2 = Base(), Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_unique_id(self):
        self.assertEqual(Base(15).id, 15)

    def test_nb_instances_after_unique_id(self):
        base1, base2, base3 = Base(), Base(15), Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_id_public(self):
        base = Base(15)
        base.id = 12
        self.assertEqual(base.id, 12)

    def test_nb_objects_private(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_non_integer_id(self):
        non_integer_values = ["str", 15.5, complex(15), {"a": 2, "b": 4},
                              True, [2, 4, 8], (2, 4), {2, 4, 8},
                              frozenset({2, 4, 8}), range(15), b'Python',
                              bytearray(b'Python'), memoryview(b'Python'),
                              float('inf'), float('nan')]

        for value in non_integer_values:
            self.assertIs(Base(value).id, value)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(2, 4)


class TestBaseToJsonStringMethod(unittest.TestCase):
    """
    Test cases for the to_json_string method of the Base class.
    """

    def test_to_json_string_return_type(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        json_string = Base.to_json_string([rectangle.to_dictionary()])
        self.assertIsInstance(json_string, str)

        square = Square(10, 2, 3, 4)
        json_string = Base.to_json_string([square.to_dictionary()])
        self.assertIsInstance(json_string, str)

    def test_to_json_string_rectangle(self):
        rectangle = Rectangle(10, 7, 2, 8, 6)
        json_string = Base.to_json_string([rectangle.to_dictionary()])
        self.assertEqual(json_string, json.dumps([rectangle.to_dictionary()]))

    def test_to_json_string_rectangle_multiple_dicts(self):
        rectangle1 = Rectangle(2, 3, 5, 19, 2)
        rectangle2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rectangle1.to_dictionary(), rectangle2.to_dictionary()]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, json.dumps(list_dicts))

    def test_to_json_string_square(self):
        square = Square(10, 2, 3, 4)
        json_string = Base.to_json_string([square.to_dictionary()])
        self.assertEqual(json_string, json.dumps([square.to_dictionary()]))

    def test_to_json_string_square_multiple_dicts(self):
        square1 = Square(10, 2, 3, 4)
        square2 = Square(4, 5, 21, 2)
        list_dicts = [square1.to_dictionary(), square2.to_dictionary()]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, json.dumps(list_dicts))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBaseSaveToFileMethod(unittest.TestCase):
    """
    Test cases for the save_to_file method of the Base class.
    """

    @classmethod
    def tearDownClass(cls):
        file_list = ["Rectangle.json", "Square.json", "Base.json"]
        for file_name in file_list:
            try:
                os.remove(file_name)
            except IOError:
                pass

    def test_save_to_file(self):
        rectangle = Rectangle(10, 7, 2, 8, 5)
        square = Square(10, 7, 2, 8)

        # Test save_to_file for Rectangle
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [rectangle.to_dictionary()])

        # Test save_to_file for Square
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [square.to_dictionary()])

    def test_save_to_file_multiple_objects(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 5)
        rectangle2 = Rectangle(2, 4, 1, 2, 3)
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)

        # Test save_to_file for Rectangle
        Rectangle.save_to_file([rectangle1, rectangle2])
        with open("Rectangle.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [rectangle1.to_dictionary(),
                                    rectangle2.to_dictionary()])

        # Test save_to_file for Square
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [square1.to_dictionary(),
                                    square2.to_dictionary()])

    def test_save_to_file_cls_name_for_filename(self):
        square = Square(10, 7, 2, 8)

        # Test save_to_file with Base class (filename should be 'Base.json')
        Base.save_to_file([square])
        with open("Base.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [square.to_dictionary()])

    def test_save_to_file_overwrite(self):
        square1 = Square(9, 2, 39, 2)

        # Save square1 to file
        Square.save_to_file([square1])

        # Modify square1 and save again to the same file
        square1 = Square(10, 7, 2, 8)
        Square.save_to_file([square1])

        # Check if file size remains the same (no new entries)
        with open("Square.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [square1.to_dictionary()])

    def test_save_to_file_with_none_or_empty_list(self):
        # Test save_to_file with None input
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

        # Test save_to_file with empty list
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_invalid_args(self):
        # Test save_to_file with no arguments
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        # Test save_to_file with more than one argument
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBaseFromJsonStringMethod(unittest.TestCase):
    """
    Test cases for the from_json_string method of the Base class.
    """

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBaseCreateMethod(unittest.TestCase):
    """
    Test cases for the create method of the Base class.
    """

    def test_create_rectangle_original(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dictionary = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangle2))

    def test_create_rectangle_new(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dictionary = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rectangle2))

    def test_create_rectangle_is(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dictionary = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dictionary)
        self.assertIsNot(rectangle1, rectangle2)

    def test_create_rectangle_equals(self):
        rectangle1 = Rectangle(3, 5, 1, 2, 7)
        rectangle1_dictionary = rectangle1.to_dictionary()
        rectangle2 = Rectangle.create(**rectangle1_dictionary)
        self.assertNotEqual(rectangle1, rectangle2)

    def test_create_square_original(self):
        square1 = Square(3, 5, 1, 7)
        square1_dictionary = square1.to_dictionary()
        square2 = Square.create(**square1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square2))

    def test_create_square_new(self):
        square1 = Square(3, 5, 1, 7)
        square1_dictionary = square1.to_dictionary()
        square2 = Square.create(**square1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(square2))

    def test_create_square_is(self):
        square1 = Square(3, 5, 1, 7)
        square1_dictionary = square1.to_dictionary()
        square2 = Square.create(**square1_dictionary)
        self.assertIsNot(square1, square2)

    def test_create_square_equals(self):
        square1 = Square(3, 5, 1, 7)
        square1_dictionary = square1.to_dictionary()
        square2 = Square.create(**square1_dictionary)
        self.assertNotEqual(square1, square2)


class TestBaseLoadFromFileMethod(unittest.TestCase):
    """
    Test cases for the load_from_file method of the Base class.
    """

    @classmethod
    def tearDown(cls):
        file_list = ["Base.json", "Rectangle.json", "Square.json"]
        for file_name in file_list:
            try:
                os.remove(file_name)
            except IOError:
                pass

    def test_load_from_file_first_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(square1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file([square1, square2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(square2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rectangle1, rectangle2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBaseSaveToFileCsvMethod(unittest.TestCase):
    """
    Test cases for the save_to_file_csv method of the Base class.
    """

    @classmethod
    def tearDown(cls):
        file_list = ["Base.csv", "Rectangle.csv", "Square.csv"]
        for file_name in file_list:
            try:
                os.remove(file_name)
            except IOError:
                pass

    def test_save_to_file_csv_one_rectangle(self):
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rectangle])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 5)
        rectangle2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n3,2,4,1,2", f.read())

    def test_save_to_file_csv_one_square(self):
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([square1, square2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        square = Square(10, 7, 2, 8)
        Base.save_to_file_csv([square])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        square = Square(9, 2, 39, 2)
        Square.save_to_file_csv([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file_csv([square])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseLoadFromFileCsvMethod(unittest.TestCase):
    """
    Test cases for the load_from_file_csv method of the Base class.
    """

    @classmethod
    def tearDown(cls):
        file_list = ["Base.csv", "Rectangle.csv", "Square.csv"]
        for file_name in file_list:
            try:
                os.remove(file_name)
            except IOError:
                pass

    def test_load_from_file_csv_first_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rectangle2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        rectangle1 = Rectangle(10, 7, 2, 8, 1)
        rectangle2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rectangle1, rectangle2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == '__main__':
    unittest.main()
