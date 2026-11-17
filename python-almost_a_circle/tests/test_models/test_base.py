#!/usr/bin/python3
"""Unit tests for the Base class."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseIds(unittest.TestCase):
    """Tests the id management of Base."""

    def test_sequential_ids(self):
        """Ids are generated one after the other."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, b2.id + 1)

    def test_given_id(self):
        """A given id is used as is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_consume_counter(self):
        """A given id does not increment the counter."""
        b1 = Base()
        Base(89)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)

    def test_none_id(self):
        """Passing None generates an id."""
        b1 = Base(None)
        self.assertIsInstance(b1.id, int)

    def test_zero_and_negative_id(self):
        """Any integer id is accepted."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)

    def test_private_counter(self):
        """The counter is a private class attribute."""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertFalse(hasattr(Base, "nb_objects"))

    def test_too_many_arguments(self):
        """Base takes at most one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseJsonString(unittest.TestCase):
    """Tests to_json_string and from_json_string."""

    def test_to_json_string_none(self):
        """None gives an empty JSON list."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list gives an empty JSON list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """A list of dictionaries is serialized."""
        result = Base.to_json_string([{"id": 1, "x": 2}])
        self.assertEqual(json.loads(result), [{"id": 1, "x": 2}])
        self.assertIsInstance(result, str)

    def test_to_json_string_two_dicts(self):
        """Several dictionaries are serialized in order."""
        result = Base.to_json_string([{"id": 1}, {"id": 2}])
        self.assertEqual(json.loads(result), [{"id": 1}, {"id": 2}])

    def test_from_json_string_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """A JSON list is turned back into a list of dictionaries."""
        result = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertEqual(result, [{"id": 89, "width": 10}])
        self.assertIsInstance(result, list)

    def test_round_trip(self):
        """to_json_string and from_json_string are inverses."""
        data = [{"id": 7, "width": 1, "height": 7}]
        text = Base.to_json_string(data)
        self.assertEqual(Base.from_json_string(text), data)

    def test_from_json_string_invalid(self):
        """Invalid JSON raises an error."""
        with self.assertRaises(ValueError):
            Base.from_json_string("{not json")


class TestBaseFiles(unittest.TestCase):
    """Tests save_to_file and load_from_file."""

    def tearDown(self):
        """Remove the files created by the tests."""
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_save_rectangles(self):
        """Rectangles are saved to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """Squares are saved to Square.json."""
        s1 = Square(5, 0, 0, 1)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [s1.to_dictionary()])

    def test_save_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_empty_list(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_overwrites(self):
        """An existing file is overwritten."""
        Rectangle.save_to_file([Rectangle(1, 1, 0, 0, 1)])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_load_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """Rectangles are loaded back with the same attributes."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertIsInstance(loaded[0], Rectangle)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))
        self.assertIsNot(loaded[0], r1)

    def test_load_squares(self):
        """Squares are loaded back with the same attributes."""
        s1 = Square(5, 0, 0, 5)
        s2 = Square(7, 9, 1, 6)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])
        self.assertIsInstance(loaded[1], Square)


class TestBaseCreate(unittest.TestCase):
    """Tests the create class method."""

    def test_create_rectangle(self):
        """A rectangle is created from a dictionary."""
        r1 = Rectangle(3, 5, 1, 0, 9)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r2), "[Rectangle] (9) 1/0 - 3/5")
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """A square is created from a dictionary."""
        s1 = Square(4, 2, 3, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s2), "[Square] (7) 2/3 - 4")
        self.assertIsInstance(s2, Square)

    def test_create_partial(self):
        """Missing keys keep the dummy values."""
        r = Rectangle.create(id=5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)


if __name__ == "__main__":
    unittest.main()
