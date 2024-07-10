#!/usr/bin/python3
"""Module for finding a peak in a list of integers."""


def find_peak(list_of_integers):
    """
    Finds a peak (local maximum) in an unsorted list of integers.

    Args:
        list_of_integers: A list of unsorted integers.

    Returns:
        The index of a peak element in the list, or None if no peak is found.
    """

    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
