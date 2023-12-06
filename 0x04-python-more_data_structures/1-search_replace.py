#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the elements of the original list
    for element in my_list:
        # Replace the element if it matches the search element
        new_list.append(replace if element == search else element)

    return new_list
