#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests the constructor and the inheritance."""

    def test_is_a_base(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_attributes(self):
        """All attributes are stored."""
        r = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 3, 4, 12))

    def test_defaults(self):
        """x and y default to 0 and the id is generated."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual((r1.x, r1.y), (0, 0))
        self.assertEqual(r2.id, r1.id + 1)

    def test_private_attributes(self):
        """The attributes are stored privately."""
        r = Rectangle(1, 2)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)

    def test_missing_arguments(self):
        """width and height are mandatory."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_arguments(self):
        """At most five arguments are accepted."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangleValidation(unittest.TestCase):
    """Tests the validation of every attribute."""

    def test_width_type(self):
        """width must be an integer."""
        for bad in ("2", 2.5, None, [2], {2}, True):
            with self.assertRaises(TypeError) as error:
                Rectangle(bad, 2)
            self.assertEqual(str(error.exception), "width must be an integer")

    def test_height_type(self):
        """height must be an integer."""
        with self.assertRaises(TypeError) as error:
            Rectangle(10, "2")
        self.assertEqual(str(error.exception), "height must be an integer")

    def test_x_type(self):
        """x must be an integer."""
        with self.assertRaises(TypeError) as error:
            Rectangle(10, 2, {})
        self.assertEqual(str(error.exception), "x must be an integer")

    def test_y_type(self):
        """y must be an integer."""
        with self.assertRaises(TypeError) as error:
            Rectangle(10, 2, 3, "4")
        self.assertEqual(str(error.exception), "y must be an integer")

    def test_width_value(self):
        """width must be greater than 0."""
        for bad in (0, -10):
            with self.assertRaises(ValueError) as error:
                Rectangle(bad, 2)
            self.assertEqual(str(error.exception), "width must be > 0")

    def test_height_value(self):
        """height must be greater than 0."""
        with self.assertRaises(ValueError) as error:
            Rectangle(10, 0)
        self.assertEqual(str(error.exception), "height must be > 0")

    def test_x_value(self):
        """x must be 0 or more."""
        with self.assertRaises(ValueError) as error:
            Rectangle(10, 2, -1)
        self.assertEqual(str(error.exception), "x must be >= 0")

    def test_y_value(self):
        """y must be 0 or more."""
        with self.assertRaises(ValueError) as error:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def test_setters_validate(self):
        """The setters apply the same validation."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.height = "3"
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r.y = -3

    def test_setters_assign(self):
        """Valid values are assigned by the setters."""
        r = Rectangle(1, 1)
        r.width, r.height, r.x, r.y = 5, 6, 7, 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_order_of_validation(self):
        """width is validated before height, x and y."""
        with self.assertRaises(TypeError) as error:
            Rectangle("1", "2", "3", "4")
        self.assertEqual(str(error.exception), "width must be an integer")


class TestRectangleArea(unittest.TestCase):
    """Tests the area method."""

    def test_area(self):
        """area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_after_update(self):
        """area follows attribute changes."""
        r = Rectangle(2, 2)
        r.width = 5
        self.assertEqual(r.area(), 10)

    def test_area_no_arguments(self):
        """area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Tests the display method."""

    def capture(self, rectangle):
        """Return what display prints."""
        output = io.StringIO()
        with redirect_stdout(output):
            rectangle.display()
        return output.getvalue()

    def test_display_simple(self):
        """A rectangle is drawn with #."""
        self.assertEqual(self.capture(Rectangle(4, 6)), "####\n" * 6)
        self.assertEqual(self.capture(Rectangle(2, 2)), "##\n##\n")

    def test_display_one(self):
        """A 1x1 rectangle is a single #."""
        self.assertEqual(self.capture(Rectangle(1, 1)), "#\n")

    def test_display_x(self):
        """x adds spaces before each line."""
        self.assertEqual(self.capture(Rectangle(3, 2, 1, 0)), " ###\n ###\n")

    def test_display_y(self):
        """y adds new lines before the rectangle."""
        self.assertEqual(self.capture(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_display_x_and_y(self):
        """x and y are both honoured."""
        self.assertEqual(self.capture(Rectangle(1, 1, 3, 1)), "\n   #\n")


class TestRectangleStr(unittest.TestCase):
    """Tests the string representation."""

    def test_str(self):
        """__str__ follows the expected format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_str_defaults(self):
        """Default x and y are shown as 0."""
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))

    def test_print(self):
        """print uses __str__."""
        output = io.StringIO()
        with redirect_stdout(output):
            print(Rectangle(1, 2, 3, 4, 5))
        self.assertEqual(output.getvalue(), "[Rectangle] (5) 3/4 - 1/2\n")


class TestRectangleUpdate(unittest.TestCase):
    """Tests the update method."""

    def test_update_args(self):
        """Positional arguments are taken in order."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        """update without arguments changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_extra_args_ignored(self):
        """Extra positional arguments are ignored."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10, 11)
        self.assertEqual(str(r), "[Rectangle] (6) 9/10 - 7/8")

    def test_update_args_validation(self):
        """Positional arguments are validated."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.update(1, "2")
        with self.assertRaises(ValueError):
            r.update(1, 2, -3)

    def test_update_kwargs(self):
        """Keyword arguments are applied in any order."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kwargs_skipped_with_args(self):
        """Keyword arguments are ignored when positional ones exist."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(9, width=7)
        self.assertEqual(str(r), "[Rectangle] (9) 3/4 - 1/2")

    def test_update_unknown_kwarg(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(color="red")
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_kwargs_validation(self):
        """Keyword arguments are validated."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2).update(height=0)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests the to_dictionary method."""

    def test_to_dictionary(self):
        """The dictionary holds the five attributes."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_feeds_update(self):
        """The dictionary can be given to update."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r2), str(r1))
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_is_a_copy(self):
        """Changing the dictionary does not change the rectangle."""
        r = Rectangle(1, 2)
        d = r.to_dictionary()
        d["width"] = 50
        self.assertEqual(r.width, 1)


if __name__ == "__main__":
    unittest.main()
