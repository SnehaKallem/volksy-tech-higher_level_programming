#!/usr/bin/python3
"""read text file"""


def read_file(filename=""):
    """with"""
    with open(filename, encoding='UTF-8') as file:
        for line in file:
            print(line, end="")
