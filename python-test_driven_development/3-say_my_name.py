#!/usr/bin/python3
"""Module 3-say_my_name.

This module provides say_my_name, a function that prints a greeting of
the form "My name is <first name> <last name>" after checking that both
names are strings.
"""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first_name> <last_name>".

    Both arguments must be strings, otherwise a TypeError is raised.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
