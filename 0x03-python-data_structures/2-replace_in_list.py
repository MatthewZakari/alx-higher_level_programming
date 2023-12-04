#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # return the original list
        return my_list
    else:
        # replace the element at idx with the new element
        my_list[idx] = element
        # return the modified list
        return my_list
