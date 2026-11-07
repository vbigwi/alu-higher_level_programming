#!/usr/bin/python3
"""Module 6-base_geometry: defines BaseGeometry with an abstract area."""


class BaseGeometry:
    """Base class for geometry shapes that must implement area()."""

    def area(self):
        """Raise an Exception because the area is not implemented here."""
        raise Exception("area() is not implemented")
