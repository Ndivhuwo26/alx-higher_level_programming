#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    Parameters:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
