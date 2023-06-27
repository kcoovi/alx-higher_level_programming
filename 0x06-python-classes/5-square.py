#!/usr/bin/python3
"""Comment"""


class Square:
    """Comment"""

    def __init__(self, size):
        """Comment"""
        self.size = size

    @property
    def size(self):
        """Comment"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Comment"""
        return (self.__size * self.__size)

    def my_print(self):
        """Comment"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
