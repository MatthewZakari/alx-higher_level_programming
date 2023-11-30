#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_digit = abs(number) % 10  # Get the last digit
if number < 0:
    lst_digit = -lst_digit
print(f"Last digit of {number:d} is {lst_digit:d} and is ", end=" ")
if lst_digit > 5:
    print("greater than 5")
elif lst_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
