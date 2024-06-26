#!/usr/bin/python3

"""The  JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Makes a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
