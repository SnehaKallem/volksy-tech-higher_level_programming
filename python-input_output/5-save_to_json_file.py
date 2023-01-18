#!/usr/bin/python3
"""string"""
import json


def save_to_json_file(my_obj, filename):
    """with"""
    with open(filename, 'w' , encoding="UTF-8") as f:
        json.dump(my_obj, f)
