#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class
        with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
