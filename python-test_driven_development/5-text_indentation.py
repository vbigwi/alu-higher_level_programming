#!/usr/bin/python3
"""Module 5-text_indentation.

This module provides text_indentation, a function that prints a text
with two new lines after every '.', '?' and ':' character and without
leading or trailing spaces on each printed line.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    text must be a string, otherwise a TypeError is raised.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    result = ""
    for character in text:
        result += character
        if character in ".?:":
            result += "\n\n"
    lines = result.split("\n")
    print("\n".join(line.strip() for line in lines), end="")
