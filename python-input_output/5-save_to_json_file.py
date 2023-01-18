#!/usr/bin/python3
"""string"""


def save_to_json_file(my_obj, filename):
    """with"""
    with open(filename, 'w' , encoding="utf-8") as f:
        json.dump(my_obj, f)
