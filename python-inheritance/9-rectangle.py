#!/usr/bin/python3
"""Module 9-rectangle: defines a full Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated private width and height and an area."""

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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
