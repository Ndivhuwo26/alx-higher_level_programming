#!/usr/bin/python3

""" The JSON-to-object function."""
import json


def from_json_string(my_str):
    """The Python object representation of a JSON string."""
    return json.loads(my_str)

