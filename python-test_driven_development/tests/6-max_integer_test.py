#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """The max is the last element of an ascending list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """The max is found wherever it is in the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """The max can be the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """The max can be in the middle of the list."""
        self.assertEqual(max_integer([1, 9, 3]), 9)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling without argument uses the empty default list."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A single element is the max."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Negative numbers are compared correctly."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_sign_numbers(self):
        """Positive and negative numbers mixed together."""
        self.assertEqual(max_integer([-5, 0, 3, -1]), 3)

    def test_all_equal(self):
        """A list of equal numbers returns that number."""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_duplicate_max(self):
        """The max can appear several times."""
        self.assertEqual(max_integer([1, 5, 5, 3]), 5)

    def test_floats(self):
        """Floats are compared like integers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_ints_and_floats(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Very large integers are handled."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 19]), 10 ** 20)

    def test_strings(self):
        """Strings are compared alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_single_string(self):
        """A string is a sequence of characters."""
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_lists(self):
        """Lists are compared element by element."""
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_none_in_list(self):
        """None cannot be compared with integers."""
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])

    def test_mixed_types(self):
        """Integers and strings cannot be compared."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 2])

    def test_not_a_list(self):
        """An integer has no length so a TypeError is raised."""
        with self.assertRaises(TypeError):
            max_integer(42)


if __name__ == '__main__':
    unittest.main()
