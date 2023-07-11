#!/usr/bin/python3
"""Main"""
import json


def load_from_json_file(filename):
    """Doc"""
    with open(filename) as myfile:
        return (json.load(myfile))
