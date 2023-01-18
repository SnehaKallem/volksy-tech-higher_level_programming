#!/usr/bin/python3
"""string"""


def append_write(filename="", text=""):
    """with"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
