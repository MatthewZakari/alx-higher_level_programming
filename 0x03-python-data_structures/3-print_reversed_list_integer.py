#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # loop through the list in reverse order
    for i in range(len(my_list) - 1, -1, -1):
        # use str.format() to print the integer
        print("{:d}".format(my_list[i]))
