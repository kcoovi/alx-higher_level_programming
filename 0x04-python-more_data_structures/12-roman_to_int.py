#!/usr/bin/python3
def subtract_max_value(num_list):
    subtract_val = 0
    max_val = max(num_list)

    for num in num_list:
        if max_val > num:
            subtract_val += num

    return max_val - subtract_val


def roman_to_int(roman_str):
    if not roman_str:
        return 0

    if not isinstance(roman_str, str):
        return 0

    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    roman_keys = list(roman_nums.keys())

    result = 0
    last_val = 0
    num_list = [0]

    for char in roman_str:
        for r_key in roman_keys:
            if r_key == char:
                if roman_nums.get(char) <= last_val:
                    result += subtract_max_value(num_list)
                    num_list = [roman_nums.get(char)]
                else:
                    num_list.append(roman_nums.get(char))

                last_val = roman_nums.get(char)

    result += subtract_max_value(num_list)

    return result
