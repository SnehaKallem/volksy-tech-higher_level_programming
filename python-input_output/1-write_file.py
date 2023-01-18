#!/usr/bin/python3
"""string"""


def write_file(filename="", text=""):
    """num of char"""
    character=0
    with open(filename, encoding='UTF-8') as file:
        for line in file:
            character = character + 1
        return character
