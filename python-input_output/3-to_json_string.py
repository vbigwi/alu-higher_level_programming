#!/usr/bin/python3
"""Module 3-to_json_string: serializes an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of my_obj."""
    return json.dumps(my_obj)
