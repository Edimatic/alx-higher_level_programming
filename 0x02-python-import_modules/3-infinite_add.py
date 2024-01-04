#!usr/bin/python
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for v in range(len(sys.argv) - 1):
        total += int(sys.argv[v + 1])
    print("{}".format(total))
