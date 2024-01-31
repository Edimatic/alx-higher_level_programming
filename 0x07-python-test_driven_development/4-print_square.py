#!/usr/bin/python3
"""

This module contain a function that prints a square

"""


def print_square(put):
    """This function prints a square with the character #

    Args:
        size (int): This represents the length of the square

    Raises:
        TypeError: If the put size is not an integer
        TypeError: If the put size is a float and less than zero
        ValueError: If the put size is less than zero

    """

    if not isinstance(put, int):
        raise TypeError("the put type must be an integer")
    elif put < 0:
        raise ValueError("the put must be >= 0")
    elif isinstance(put, float) and put < 0:
        raise TypeError("the put type must be an integer")
    for n in range(0, put):
        for m in range(put):
            print("#", end="")
        print("")
