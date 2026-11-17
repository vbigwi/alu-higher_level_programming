#!/usr/bin/python3
"""Module 4-print_square.

This module provides print_square, a function that draws a square of a
given size on standard output using the # character, one row per line.
"""


def print_square(size):
    """Print a square of side size made of the # character.

    size must be a positive integer, otherwise an exception is raised.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
