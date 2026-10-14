#!/usr/bin/env python3
"""Defines classes for shapes with abstract base classes"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Defines abstract class for Shape"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Initialises Circle subclass of Shape"""

    def __init__(self, radius):
        """Represents a circle defined by its radius"""
        self.__radius = radius

    def area(self):
        """Returns area of circle"""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """Returns perimeter of cirlce"""
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    """Initialises Rectangle subclass of Shape"""

    def __init__(self, width, height):
        """Represents a rectangle defined by its height and width"""
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of rectangle"""
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """Prints area and perimeter of a shape"""
    print("Area: ", shape.area())
    print("Perimeter: ", shape.perimeter())
