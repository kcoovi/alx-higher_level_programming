#!/usr/bin/python3

def no_c(my_string):
    """Remove characters"""
    newStr = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            newStr += char
    return newStr
