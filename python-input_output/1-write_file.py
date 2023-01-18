#!/usr/bin/python3
"""string"""


def write_file(filename="", text=""):
    """num of char"""
    with open(filename, 'w', encoding="utf-8") as wf:
        wf.write(text)
        return len(text)
