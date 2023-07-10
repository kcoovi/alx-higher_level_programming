#!/usr/bin/python3
"""Function"""


def inherits_from(obj, a_class):
    """Doc"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
