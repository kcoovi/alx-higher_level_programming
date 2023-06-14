#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete key"""
    new_dictionary = a_dictionary.copy()
    new_dictionary.pop(key, None)
    return new_dictionary
