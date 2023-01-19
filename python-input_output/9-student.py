#!/usr/bin/python3
"""dict"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary"""
        return self.__dict__
