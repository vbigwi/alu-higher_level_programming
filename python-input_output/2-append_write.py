#!/usr/bin/python3
"""Module 2-append_write: appends a string to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append text at the end of filename and return the char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
