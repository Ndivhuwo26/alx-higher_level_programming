#!/usr/bin/python3

""" A text file-reading function."""
def read_file(filename=""):
    """Write the provided text to a UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
