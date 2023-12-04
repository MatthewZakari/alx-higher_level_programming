#!/usr/bin/python3

def no_c(my_string):
    # initialize an empty string
    new_string = ""
    # loop through each character in the original string
    for char in my_string:
        # check if the character is not c or C
        if char != "c" and char != "C":
            # append the character to the new string
            new_string += char
    # return the new string
    return new_string
