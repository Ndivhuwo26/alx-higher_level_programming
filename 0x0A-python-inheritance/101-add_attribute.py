#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, att, value):
    """ Adds a new attribute to an object if possible.

    Parameters:
        obj: Any Python object.
        attr (str): The name of the attribute to be added.
        value: The value of the attribute to be added.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
