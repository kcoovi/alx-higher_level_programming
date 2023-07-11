#!/usr/bin/python3
"""Main"""
import json


def save_to_json_file(my_obj, filename):
    """Doc"""
    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
