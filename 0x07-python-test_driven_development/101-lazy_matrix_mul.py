#!/usr/bin/python3
"""Module for Multiply two matrices."""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the resulting matrix.

    Args:
        - m_a (list of lists): The first matrix.
        - m_b (list of lists): The second matrix.
    Returns:
         - list of lists: The result of multiplying m_a and m_b.
    """

    return numpy.matmul(m_a, m_b)
