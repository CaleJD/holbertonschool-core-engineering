#!/usr/bin/env python3
"""Defines a subclass for a rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialize a rectangle with a validated width and height."""

    def __init__(self, width, height):
        """Represents a rectangle defined by its width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the description of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
