#!/usr/bin/python3


def magic_calculation(a, b):
    output = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise ValueError('Too far')
            output += a ** b / i
        except ValueError:
            output = b + a
            break

    return output
