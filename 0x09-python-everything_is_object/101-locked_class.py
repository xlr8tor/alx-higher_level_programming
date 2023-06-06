#!/usr/bin/python3


"""a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""


class LockedClass:
    """LockedClass instance"""

    __slots__ = ("first_name")

    def __init__(self):
        pass
