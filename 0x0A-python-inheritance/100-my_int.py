#!/usr/bin/python3


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """switch == with !="""
        return !(self.real == other)

    def __ne__(self, value):
        """switch != with =="""
        return !(self.real != other)
