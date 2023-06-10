#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace elements"""
    if not (0 <= idx < len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list
