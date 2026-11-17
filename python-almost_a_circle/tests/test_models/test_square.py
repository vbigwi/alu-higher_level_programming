#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests the constructor and the inheritance."""

    def test_inheritance(self):
        """Square inherits from Rectangle and Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_attributes(self):
        """size sets both width and height."""
        s = Square(5, 1, 2, 3)
        self.assertEqual((s.width, s.height, s.x, s.y, s.id), (5, 5, 1, 2, 3))
        self.assertEqual(s.size, 5)

    def test_defaults(self):
        """x and y default to 0 and the id is generated."""
        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual((s1.x, s1.y), (0, 0))
        self.assertEqual(s2.id, s1.id + 1)

    def test_no_new_attributes(self):
        """Square reuses the private attributes of Rectangle."""
        s = Square(3)
        self.assertEqual(s._Rectangle__width, 3)
        self.assertFalse(hasattr(s, "_Square__size"))

    def test_missing_argument(self):
        """size is mandatory."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_arguments(self):
        """At most four arguments are accepted."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareValidation(unittest.TestCase):
    """Tests the validation inherited from Rectangle."""

    def test_size_type(self):
        """size must be an integer, reported as width."""
        with self.assertRaises(TypeError) as error:
            Square("9")
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_size_value(self):
        """size must be greater than 0."""
        with self.assertRaises(ValueError) as error:
            Square(0)
        self.assertEqual(str(error.exception), "width must be > 0")
        with self.assertRaises(ValueError):
            Square(-2)

    def test_x_and_y(self):
        """x and y are validated like in Rectangle."""
        with self.assertRaises(TypeError) as error:
            Square(1, "2")
        self.assertEqual(str(error.exception), "x must be an integer")
        with self.assertRaises(ValueError) as error:
            Square(1, 0, -1)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def test_size_setter(self):
        """The size setter updates width and height together."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height, s.size), (10, 10, 10))

    def test_size_setter_validation(self):
        """The size setter validates like width."""
        s = Square(5)
        with self.assertRaises(TypeError) as error:
            s.size = "9"
        self.assertEqual(str(error.exception), "width must be an integer")
        with self.assertRaises(ValueError):
            s.size = 0


class TestSquareBehaviour(unittest.TestCase):
    """Tests area, display and __str__."""

    def test_area(self):
        """area is size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)

    def test_str(self):
        """__str__ follows the Square format."""
        self.assertEqual(str(Square(5, 0, 0, 1)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(3, 1, 3, 3)), "[Square] (3) 1/3 - 3")

    def test_display(self):
        """display draws the square honouring x and y."""
        output = io.StringIO()
        with redirect_stdout(output):
            Square(2, 1, 1).display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")


class TestSquareUpdate(unittest.TestCase):
    """Tests the update method."""

    def test_update_args(self):
        """Positional arguments are id, size, x, y."""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Keyword arguments are applied in any order."""
        s = Square(2, 3, 4, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/4 - 2")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_kwargs_skipped_with_args(self):
        """Keyword arguments are ignored when positional ones exist."""
        s = Square(5, 0, 0, 1)
        s.update(2, size=9)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 5")

    def test_update_validation(self):
        """Values are validated by the setters."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "2")
        with self.assertRaises(ValueError):
            s.update(size=-1)

    def test_update_extra_args_ignored(self):
        """Extra positional arguments are ignored."""
        s = Square(5, 0, 0, 1)
        s.update(2, 3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (2) 4/5 - 3")


class TestSquareToDictionary(unittest.TestCase):
    """Tests the to_dictionary method."""

    def test_to_dictionary(self):
        """The dictionary holds id, size, x and y."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})
        self.assertNotIn("width", s.to_dictionary())

    def test_to_dictionary_feeds_update(self):
        """The dictionary can be given to update."""
        s1 = Square(10, 2, 1, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s2), str(s1))
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
