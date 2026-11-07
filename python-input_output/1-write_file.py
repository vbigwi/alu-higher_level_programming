#!/usr/bin/python3
"""Module 1-write_file: writes a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write text to filename, overwriting it, and return the char count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
