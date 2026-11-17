#!/usr/bin/python3
"""Module square: defines the Square class built on top of Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, which is a rectangle whose width and height are equal."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

        Args:
            size (int): the length of the sides, must be greater than 0.
            x (int): the horizontal offset, must be 0 or more.
            y (int): the vertical offset, must be 0 or more.
            id (int): the id handed to Base.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height of the square to value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the attributes from positional or keyword arguments.

        Positional arguments are taken in the order id, size, x, y.
        Keyword arguments are only used when no positional argument is given.
        """
        names = ["id", "size", "x", "y"]
        if len(args) > 0:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
