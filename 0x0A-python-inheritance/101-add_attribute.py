#!/usr/bin/python3

def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Parameters:
        obj: Any Python object.
        attr (str): The name of the attribute to be added.
        value: The value of the attribute to be added.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
