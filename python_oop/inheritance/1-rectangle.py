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
