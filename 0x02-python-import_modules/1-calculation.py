#!/usr/bin/python3
if __name__ == "__main__":
    """A program that imports functions from the file calculator_1.py, does some Maths, and prints the result"""

from calculator_1 import add, sub, mul, div

a = 10
b = 5

print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))
