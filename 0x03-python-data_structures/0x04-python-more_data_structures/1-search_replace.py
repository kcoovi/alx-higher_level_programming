#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Search and replace"""
    newList = [replace if x == search else x for x in my_list]
    return newList
