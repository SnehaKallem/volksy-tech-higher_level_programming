#!/usr/bin/python3
"""This module creates the Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of class instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of class instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

