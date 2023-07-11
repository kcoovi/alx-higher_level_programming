#!/usr/bin/python3
"""Main"""


def write_file(filename="", text=""):
    """Doc"""
    with open(filename, "w", encoding="utf-8") as myfile:
        return (myfile.write(text))
