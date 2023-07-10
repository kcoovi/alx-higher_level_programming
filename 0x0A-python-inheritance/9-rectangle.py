#!/usr/bin/python3
"""Main"""


class BaseGeometry:
    """Doc"""
    def area(self):
        """Doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Doc"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Doc"""
    def __init__(self, width, height):
        """Doc"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Doc"""
        return self.__width * self.__height

    def __str__(self):
        """Doc"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
