#!/usr/bin/python3
# 4-print_square.py
"""

This module contain a function that prints a square

"""


def print_square(in_put):
    """This function prints a square with the character #

    Args:
        size (int): This represents the length of the square

    Raises:
        TypeError: If the in_put size is not an integer
        TypeError: If the in_put size is a float and less than zero
        ValueError: If the in_put size is less than zero

    """

    if not isinstance(in_put, int):
        raise TypeError("the in_put type must be an integer")
    elif in_put < 0:
        raise ValueError("the in_put must be >= 0")
    elif isinstance(in_put, float) and in_put < 0:
        raise TypeError("the in_put type must be an integer")
    for n in range(0, in_put):
        for m in range(in_put):
            print("#", end="")
        print("")
