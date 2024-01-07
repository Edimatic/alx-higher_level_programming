#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]

# Example usage:


my_list = [1, 2, 3, 4, 5]
idx = 3
result = element_at(my_list, idx)
print("Element at index {} is {}".format(idx, result))
