#!/usr/bin/python3
"""Main"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Doc"""
    def __init__(self, size):
        """Doc"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Doc"""
        return self.__size ** 2
