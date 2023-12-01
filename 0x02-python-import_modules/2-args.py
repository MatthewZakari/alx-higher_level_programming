#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    if num_args == 0:
        print("0", end=" ")
        print("arguments.", end="\n")
    elif num_args == 1:
        print("1", end=" ")
        print("argument:", end="\n")
        print("1:", sys.argv[1])
    else:
        print(num_args, end=" ")
        print("arguments:", end="\n")
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
