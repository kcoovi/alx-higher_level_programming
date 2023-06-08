#!/usr/bin/python3
if __name__ == "__main__":
    """Perform calculations with 10 and 5"""
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("The sum of {} and {} is: {}".format(a, b, add(a, b)),
      "The difference between {} and {} is: {}".format(a, b, subtract(a, b)),
      "The product of {} and {} is: {}".format(a, b, multiply(a, b)),
      "The division of {} by {} is: {}".format(a, b, divide(a, b)), sep="\n")
