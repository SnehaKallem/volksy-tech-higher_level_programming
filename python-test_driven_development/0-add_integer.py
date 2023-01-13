#!/usr/bin/python3
"""add"""


def add_integer(a, b=98):
    """add a and b"""

    if type(a) != int and type(a) != float or a != a:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)