#!/usr/bin/python3
"""Module for Multiply two matrices."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the resulting matrix.

    Args:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    - list of lists: The result of multiplying m_a and m_b.

    Raises:
    - TypeError: If m_a or m_b is not a list, if any row in
      m_a or m_b is not a list,
      if the number of columns in any row of m_a or m_b is not consistent,
      if the elements in m_a or m_b are not integers or floats.
    - ValueError: If m_a or m_b is empty, if the number of columns in
      m_a is not equal to the number of rows in m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/100-matrix_mul.txt")
