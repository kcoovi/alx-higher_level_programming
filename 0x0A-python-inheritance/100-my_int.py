#!/usr/bin/python3
"""Main"""


class MyInt(int):
    """Doc"""
    def __new__(cls, *args, **kwargs):
        """Doc"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Doc"""
        return int(self) != other

    def __ne__(self, other):
        """Doc"""
        return int(self) == other
