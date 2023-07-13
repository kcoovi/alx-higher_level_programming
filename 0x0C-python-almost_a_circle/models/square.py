#!/usr/bin/python3
"""Main"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Doc"""

    def __init__(self, size, x=0, y=0, id=None):
        """Doc"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Doc"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        """Doc"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Doc"""
        if args and len(args) != 0:
            argument = 0
            for arg in args:
                if argument == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif argument == 1:
                    self.size = arg
                elif argument == 2:
                    self.x = arg
                elif argument == 3:
                    self.y = arg
                argument += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Doc"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
