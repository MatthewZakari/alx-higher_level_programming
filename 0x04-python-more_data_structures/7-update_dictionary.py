#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Update the value if the key already exists
    # Otherwise, create a new key-value pair
    a_dictionary[key] = value
    return a_dictionary 
