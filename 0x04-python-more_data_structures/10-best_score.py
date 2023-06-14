#!/usr/bin/python3
def best_score(a_dictionary):
    """Best score"""
    if not a_dictionary:
        return None
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
