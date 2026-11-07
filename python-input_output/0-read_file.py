#!/usr/bin/python3
"""Module 0-read_file: prints the content of a UTF-8 text file."""


def read_file(filename=""):
    """Read the text file filename and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
