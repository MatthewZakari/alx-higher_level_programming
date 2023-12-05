#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                # Print the number with formatting and a space
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
                print()
