#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: The name of the file to be read.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
