#!/usr/bin/python3
"""Module 0-add_integer.

This module provides a single function, add_integer, that adds two
numbers after casting them to integers. Non numeric arguments are
rejected with a TypeError so the caller always gets an integer back.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Floats are cast to integers first; other types raise a TypeError.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
