#!/usr/bin/python3
"""inheritance"""


def inherits_from(obj, a_class):
    """True or Flase"""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
