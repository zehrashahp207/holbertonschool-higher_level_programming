#!/usr/bin/python3
"""
This module defines a Student class with serialization
and deserialization functionality.
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.
        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using a dictionary (json).
        """
        for key in json:
            setattr(self, key, json[key])
