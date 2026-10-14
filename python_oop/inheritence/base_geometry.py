#!/usr/bin/env python3

from dataclasses import Type
class BaseGeometry:
    def area(self):
        return self.area
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError ("<name> must be an integer")
        if value < 0:
            raise ValueError ("<name> must be greater than 0")
