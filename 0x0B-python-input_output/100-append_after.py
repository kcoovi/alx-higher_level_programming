#!/usr/bin/python3
"""Main"""


def append_after(filename="", search_string="", new_string=""):
    """Doc"""
    text = ""
    with open(filename) as myfile_r:
        for line in myfile_r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as myfile_w:
        myfile_w.write(text)
