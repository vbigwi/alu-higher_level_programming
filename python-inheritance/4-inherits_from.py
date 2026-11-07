#!/usr/bin/python3
"""Module 4-inherits_from: checks strict subclass membership of an object."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a strict subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
