#!/usr/bin/env python3
"""Defines a base class for geometric shapes"""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Subclasses must implement this method."""
        return "area() is not implemented"

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
