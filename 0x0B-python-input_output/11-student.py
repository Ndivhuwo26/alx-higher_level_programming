#!/usr/bin/python3

"""this  a class Student."""


class Student:
    """this Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this will Get a dictionary representation of the Student.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """this wiil Replace all attributes of the Studen"""
        for k, v in json.items():
            setattr(self, k, v)
