#!/usr/bin/python3

if __name__ == "__main__":
"""Perform calculations using 10 and 5"""
a = 10
b = 5

from calculator_1 import add, sub, mul, div

result_sum = add(a, b)
result_diff = sub(a, b)
result_prod = mul(a, b)
result_div = div(a, b)

print(f"The sum of {a} and {b} is: {result_sum}")
print(f"The difference between {a} and {b} is: {result_diff}")
print(f"The product of {a} and {b} is: {result_prod}")
print(f"The division of {a} by {b} is: {result_div}")
