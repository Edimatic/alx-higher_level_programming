#!/usr/bin/python3
# Content: def add(a, b), def subtract(a, b), def multiply(a, b), def divide(a, b)


# Main program
a = 10
b = 5

# Importing functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Performing calculations and printing results
result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

# Printing results with a single print statement
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_subtract))
print("{} * {} = {}".format(a, b, result_multiply))
print("{} / {} = {}".format(a, b, result_divide))

