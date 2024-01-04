#!/usr/bin/python3

# File: add_0.py
# Content: def add(a, b):


# Main program
a = 1
b = 2

add_0 = __import__('add_0', globals(), locals(), ['add'], 0)
result = add_0.add(a, b)

print('{} + {} = {}'.format(a, b, result))

