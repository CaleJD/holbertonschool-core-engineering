#!/usr/bin/env python3
"""Module for the Rectangle class"""


class Rectangle:
    """This class represents a rectangle."""
    def __init__(self, size=(0, 0), position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """"Finds area of rectangle by multiplying size by size"""
        return self.__size[0] * self.__size[1]

    def __str__(self):
        if self.size[0] == 0 or self.size[1] == 0:
            return ""
        result = ""
        for _ in range(self.position[1]):
            result += "\n"
        for height in range(self.size[0]):
            result += " " * self.position[0]
            for width in range(self.size[1]):
                result += "#"
            result += "\n"
        return result

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if (
            not isinstance(size, tuple)
            or len(size) != 2
            or not all(isinstance(value, int) for value in size)
            or any(value < 0 for value in size)
        ):
            raise TypeError("size must be a tuple of 2 positive integers")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(value, int) for value in position)
            or any(value < 0 for value in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        if self.size[0] <= 0 or self.size[1] <= 0:
            print()
            return
        for space in range(self.position[1]):
            print()
        for height in range(self.size[0]):
            print(" " * self.position[0], end='')
            for width in range(self.size[1]):
                print("#", end='')
            print()