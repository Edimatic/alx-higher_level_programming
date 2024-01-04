#!usr/bin/python
import sys

def add_arguments(arguments):
    result = sum(int(arg) for arg in arguments)
    return result

if __name__ == "__main__":
    # Extracting command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Ensuring there are arguments before attempting addition
    if arguments:
        # Adding all arguments and printing the result
        result = add_arguments(arguments)
        print(result)
    else:
        print("No arguments provided.")

