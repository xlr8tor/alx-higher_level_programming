#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_items = list(a_dictionary.items())
    for k, v in list_items:
        if v == value:
            del a_dictionary[k]
    return a_dictionary
