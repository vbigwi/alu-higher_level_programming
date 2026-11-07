#!/usr/bin/python3
"""Module 4-from_json_string: deserializes a JSON string to an object."""
import json


def from_json_string(my_str):
    """Return the Python object represented by the JSON string my_str."""
    return json.loads(my_str)
