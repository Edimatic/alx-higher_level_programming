#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for g, num in enumerate(row):
            if g == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")
    if not matrix:
        print()
