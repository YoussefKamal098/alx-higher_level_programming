#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """
    Add new lines after periods, question marks, and colons in the given text.

    Args:
    - text (str): The input text that needs indentation.

    Raises:
    - TypeError: If the input `text` is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        joined = delim + "\n\n"
        text = joined.join([line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
