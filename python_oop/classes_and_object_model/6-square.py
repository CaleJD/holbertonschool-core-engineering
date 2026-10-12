#!/usr/bin/env python3
"""Module for the Square class"""


class Square:
    """This class represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """"Finds area of square by multiplying size by size"""
        return self.__size * self.__size

    def __str__(self):
        if self.size == 0:
            return ""
        result = ""
        for _ in range(self.position[1]):
            result += "\n"
        for height in range(self.size):
            result += " " * self.position[0]
            for width in range(self.size):
                result += "#"
            if height < self.size - 1:
               result += "\n"
        return result

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size cannot be negative")
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
        if self.size <= 0:
            print()
            return
        for height in range(self.size):
            print(" " * self.position[0], end='')
            for width in range(self.size):
                print("#", end='')
            print()
