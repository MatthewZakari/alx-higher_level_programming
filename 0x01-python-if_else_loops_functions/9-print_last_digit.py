def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit

    print(last_digit, end='')
    return last_digit