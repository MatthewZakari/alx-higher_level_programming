#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_set = set()

    # Iterate through the elements in the list
    for element in my_list:
        # Add the element to the set (sets automatically handle uniqueness)
        unique_set.add(element)

    # Return the sum of unique integers
    return sum(unique_set)
