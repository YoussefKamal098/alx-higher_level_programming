#!/usr/bin/python3
"""
    Unittest for max_integer function
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        The TestMaxInteger class contains unit tests for the MaxInteger class.
    """

    def test_no_arg(self):
        """test case for no args"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """test case for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """test case for one int"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """test case for identical"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """test case for max start"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """test case for  ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """test case for ordered large list"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """test case for  unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """test case for unordered large list"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                      108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """test case for positives and negatives int list"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_ints_and_floats(self):
        """test case for ints and floats"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_floats(self):
        """test case for floats"""
        self.assertEqual(
            max_integer(
                [.00123, .457568, .02345, .23423434, .45675674, .678678,
                 .867090, .74653, .5745375]), 0.86709)

    def test_numeric_string(self):
        """test case for numeric string"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """test case for  str"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """test case for  nested list"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """test case for  list of str"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """test case for inf"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """test case for nan"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """test case for nested list"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """test case for list of int and str"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """test case for none"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """test case for  dict"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """test case for int"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """test case for float"""
        with self.assertRaises(TypeError):
            max_integer(9.8)


if __name__ == '__main__':
    unittest.main()
