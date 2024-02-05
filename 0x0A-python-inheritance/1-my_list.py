#!/usr/bin/python3

class MyList(list):

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
    
    sorted_list = sorted(self)
        print(sorted_list)
