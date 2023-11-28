#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_digit = abs(number) % 10  # Get the last digit
print("Last digit of", number, "is", lst_digit, end=" ")
if lst_digit > 5:
    print("and is greater than 5")
elif lst_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
