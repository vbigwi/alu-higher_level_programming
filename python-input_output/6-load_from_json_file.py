#!/usr/bin/python3
"""Module 6-load_from_json_file: loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the Python object stored as JSON in the file filename."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
