#!/usr/bin/python3
"""Main"""
import json
import csv
import turtle


class Base():
    """Doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Doc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
       """Doc"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Doc"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dict = [op.to_dictionary() for op in list_objs]
                myfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        """Doc"""
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Doc"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        """Doc"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as myfile:
                list_dict = Base.from_json_string(myfile.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Doc"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as myfile:
            if list_objs is None or list_objs == []:
                myfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(myfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Doc"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Doc"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()

            for index in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()
        turt.color("#b5e3d8")

        for sqr in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sqr.x, sqr.y)
            turt.down()

            for index in range(2):
                turt.forward(sqr.width)
                turt.left(90)
                turt.forward(sqr.height)
                turt.left(90)
            turt.hideturtle()
