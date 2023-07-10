#!/usr/bin/python3
"""Main"""


def add_attribute(prmObject, prmName, prmValue):
    """Doc"""
    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)
