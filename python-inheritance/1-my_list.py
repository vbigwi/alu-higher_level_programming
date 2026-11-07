#!/usr/bin/python3
"""Module 1-my_list: defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list subclass that knows how to print its elements in order."""

    def print_sorted(self):
        """Print the list sorted in ascending order without changing it."""
        print(sorted(self))
