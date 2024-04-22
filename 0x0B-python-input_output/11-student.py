#!/usr/bin/python3

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve. Defaults to None.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

