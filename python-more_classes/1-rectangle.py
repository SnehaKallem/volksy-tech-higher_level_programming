#!/usr/bin/python3
"""class"""


class Rectangle:
    """width"""
    @property
    def width(self):
        self.__width = width
    @width.setter
    def width(self, value):
        if type(__width) != int:
            raise TypeError("width must be an integer")
        elif __width < 0:
            raise TypeError("width must be >= 0")
    @property
    def height(self):
        self.__height = height
    @height.setter
    def height(self, value):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
