#!/usr/bin/env python3
"""Defines a subclass of a rectangle"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Initialize a square with a validated size."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size
