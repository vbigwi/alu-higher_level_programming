#!/usr/bin/python3
"""Module rectangle: defines the Rectangle class built on top of Base."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with a validated width, height and (x, y) position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle.

        Args:
            width (int): the width, must be greater than 0.
            height (int): the height, must be greater than 0.
            x (int): the horizontal offset, must be 0 or more.
            y (int): the vertical offset, must be 0 or more.
            id (int): the id handed to Base.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def check_integer(name, value):
        """Raise a TypeError when value is not an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, which must be an integer greater than 0."""
        self.check_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, which must be an integer greater than 0."""
        self.check_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x, which must be an integer of 0 or more."""
        self.check_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y, which must be an integer of 0 or more."""
        self.check_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with # characters, honouring x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the attributes from positional or keyword arguments.

        Positional arguments are taken in the order id, width, height, x, y.
        Keyword arguments are only used when no positional argument is given.
        """
        names = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
