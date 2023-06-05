#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming " \
      "language that combines remarkable power with very clear syntax"
str_list = [str[i] for i in range(39, 67)] + [str[i] for i in range(107, 112)] + [str[i] for i in range(6)]
str = ''.join(str_list)
print(str)
