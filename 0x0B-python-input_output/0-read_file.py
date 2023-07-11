#!/usr/bin/python3
"""Main"""


def read_file(filename=""):
    '''Doc'''
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
