#!/usr/bin/python3
"""BASE module contains class base"""


class Base():
    """base class for checking id for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """base class with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts list of dictionaries to json string"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)
