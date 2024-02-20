#!/usr/bin/python3
"""
Module for Pascal's triangle Generator
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.
            Must be non-negative.

    Returns:
        list[list[int]]: A list representing the Pascal's triangle, where
            each sublist represents a row of the triangle.

    Raises:
        ValueError: If n is less than 0.
    """
    if n <= 0:
        return []

    triangle = []

    if n >= 1:
        triangle.append([1])
    if n >= 2:
        triangle.append([1, 1])

    for i in range(2, n):
        row = [0] * (len(triangle[i - 1]) + 1)

        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
