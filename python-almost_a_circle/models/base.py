#!/usr/bin/python3
"""BASE"""


class Base():
    """base class"""

    __nb_objects = 0
    
    def __int__(self, id=None):
        """base class with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
