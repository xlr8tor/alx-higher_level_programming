#!/usr/bin/python3


"""function that returns True if the object is
exactly an instance of the specified class; otherwise False."""


def inherits_from(obj, a_class):
    """check func"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
