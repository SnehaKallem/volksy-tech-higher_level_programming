#!/usr/bin/python3
"""string"""


def load_from_json_file(filename):
    """with"""
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
