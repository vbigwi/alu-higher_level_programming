#!/usr/bin/python3
"""Module 11-square: defines a Square with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square, which is a rectangle whose two sides are equal."""

    def __init__(self, size):
        """Initialize a new Square after validating its size.

        Args:
            size (int): the length of the sides, must be positive.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
