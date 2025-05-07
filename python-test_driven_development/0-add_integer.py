#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Returns the addition of a and b after checking their types.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, default is 98).

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
