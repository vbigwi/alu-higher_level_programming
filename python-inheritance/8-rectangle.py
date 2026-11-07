#!/usr/bin/python3
"""Module 8-rectangle: defines a Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated private width and height."""

    def __init__(self, width, height):
        """Initialize a new Rectangle after validating both sides.

        Args:
            width (int): the width of the rectangle, must be positive.
            height (int): the height of the rectangle, must be positive.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
