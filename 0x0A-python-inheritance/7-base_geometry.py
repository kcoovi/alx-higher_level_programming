#!/usr/bin/python3
"""Function"""


class BaseGeometry:
    def area(self):
        """Doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Doc"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
