#!/usr/bin/python3

"""A Python class-to-JSON function."""


def class_to_json(obj):
    """The dictionary represntation of a simple data structure."""
    return obj.__dict__

