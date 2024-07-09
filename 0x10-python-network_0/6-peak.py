#!/usr/bin/python3
"""Module for finding a peak in a list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers."""

    if not list_of_integers:
        return None

    peak = float('-inf')

    for integer in list_of_integers:
        if integer > peak:
            peak = integer

    return peak


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
