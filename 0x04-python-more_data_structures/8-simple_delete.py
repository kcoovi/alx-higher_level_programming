#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete keys"""
    if key in a_dictionary:
        del a_dictionary[key]
