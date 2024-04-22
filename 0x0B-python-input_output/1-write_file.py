#!/usr/bin/python3

"""A file-writing function."""

def write_file(filename="", text=""):
    """Open the file in write mode with UTF-8 encoding
    Write the text to the file
    Return the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
