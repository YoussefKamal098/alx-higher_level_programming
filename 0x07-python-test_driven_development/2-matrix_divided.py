#!/usr/bin/python3
"""Module for Divide all elements of the matrix by divisor."""


def matrix_divided(matrix, div):
    """Divide all elements of the matrix by div.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int or float): Number to divide the matrix by.

    Returns:
        list of lists: Resulting matrix with elements rounded to
        two decimal places.

    Raises:
        TypeError: If div is not an int or float.
        TypeError: If matrix is not a list of lists containing int or float.
        TypeError: If sub lists are not all the same size.
        TypeError: If matrix contains elements that are not int or float.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if type(num) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(num / div, 2) for num in row] for row in matrix]


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
