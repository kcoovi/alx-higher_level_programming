#!/usr/bin/python3
if __name__ == "__main__":
    """Perform calculations with 10 and 5"""
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("Add {} and {}: {}".format(a, b, add(a, b)),
      "Substract {} and {}: {}".format(a, b, sub(a, b)),
      "Multiply {} and {}: {}".format(a, b, mul(a, b)),
      "Divide {} by {}: {}".format(a, b, div(a, b)), sep="\n")
