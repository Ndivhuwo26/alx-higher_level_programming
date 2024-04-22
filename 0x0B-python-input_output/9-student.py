#!/usr/bin/python3

"""a class Student."""


class Student:
    """this Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """the  dictionary representation of the Student."""
        return self.

