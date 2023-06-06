#!/usr/bin/python3
def uppercase(string):
    """Print a string in uppercase."""
    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print(char, end='')
    print('')
