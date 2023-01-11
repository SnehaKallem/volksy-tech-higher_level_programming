#!/usr/bin/python3
"""String size"""


class Square:
    """size"""

    def __init__(self, size = 0):
        if type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")