#!/usr/bin/python3

if __name__ == "__main__":
"""Perform calculations using 10 and 5"""

a = 10
b = 5

import calculator_1

print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
