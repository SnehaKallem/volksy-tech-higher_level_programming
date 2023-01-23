#!/usr/bin/python3
"""BASE module contains class base"""


class Base():
    """base class for checking id for other classes"""

    __nb_objects = 0
    
    def __int__(self, id=None):
        """base class with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
