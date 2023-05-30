#!/usr/bin/python3
"""Magic Code Task"""

import math


class MagicClass:
    """Magic class from bytecode"""
    def __init(self,radius):
        if type(radius) is not int:
            raise TypeError("radius must be a number")
        if type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference:
        return 2 * math.pi * self.__radius
