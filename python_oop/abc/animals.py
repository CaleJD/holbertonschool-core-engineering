#!/usr/bin/env python3
"""Defines classes for animal, dog and cat with abstract base classes"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    def sound(self):
        """Return the sound the animal makes"""
        pass


class Dog(Animal):
    """Defines dog as a sublass of animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Defines cat as a subclass of animal"""
    def sound(self):
        return "Meow"
