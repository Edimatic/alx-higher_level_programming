#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Extracting command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Ensuring there are arguments before attempting addition
    if arguments:
        # Adding all arguments and printing the result
        result = sum(map(int, arguments))
        print(result)
    else:
        print("0")
