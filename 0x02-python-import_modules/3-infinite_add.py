#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the command-line arguments
    args = sys.argv[1:]

    # Initialize the sum to zero
    total_sum = 0

    # Iterate through arguments and add them to the sum
    for arg in args:
        total_sum += int(arg)

    # Print the result
    print(total_sum)
