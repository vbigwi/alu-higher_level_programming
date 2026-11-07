#!/usr/bin/python3
"""Module 1-square: defines a Square class with a private size."""


class Square:
    """Represents a square defined by its size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the new square (no validation).
        """
        self.__size = size
