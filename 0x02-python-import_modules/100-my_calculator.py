#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    # import the sys module to access the command-line arguments
    import sys

    # check if the number of arguments is 3
    if len(sys.argv) == 4:
        # assign the arguments to variables
        a = int(sys.argv[1])  # cast the first argument to an integer
        operator = sys.argv[2]  # assign the second argument to the operator
        b = int(sys.argv[3])  # cast the third argument to an integer

        # check if the operator is one of the valid options
        if operator in ('+', '-', '*', '/'):
            # perform the corresponding operation and print the result
            if operator == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif operator == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif operator == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif operator == '/':
                # handle the division by zero error
                try:
                    print("{} / {} = {}".format(a, b, div(a, b)))
                except ZeroDivisionError:
                    print("Cannot divide by zero")
        else:
            # print an error message and exit with the value 1
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        # print the usage message and exit with the value 1
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
