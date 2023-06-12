#!/usr/bin/python3


"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, other):
        """switch == with !="""
        return !(self.real == other)

    def __ne__(self, other):
        """switch != with =="""
        return !(self.real != other)