#!/usr/bin/python3

"""this  a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """The JSON representation of a string object."""
    return json.dumps(my_obj)

