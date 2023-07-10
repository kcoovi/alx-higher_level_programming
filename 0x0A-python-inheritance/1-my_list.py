#!/usr/bin/python3
"""Main"""


class MyList(list):
    """Doc"""
    def __init__(self):
        """Doc"""
        super().__init__()

    def print_sorted(self):
        """Doc"""
        print(sorted(self))
