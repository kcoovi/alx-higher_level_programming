#!/usr/bin/python3
"""Main"""


class Student():
    """Doc"""

    def __init__(self, first_name, last_name, age):
        """Doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Doc"""
        return (self.__dict__)
