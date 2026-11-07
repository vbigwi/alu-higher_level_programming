#!/usr/bin/python3
"""Module 8-class_to_json: dictionary description of a class instance."""


def class_to_json(obj):
    """Return the dictionary of the serializable attributes of obj."""
    return obj.__dict__
