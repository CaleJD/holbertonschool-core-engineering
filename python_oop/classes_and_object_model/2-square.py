#!/usr/bin/env python3
"""Module for the Square class"""


class Square:
    """This class represents a square."""
    def __init__(self, size=0):
        """Initialize the square with validations for the size attribute."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
