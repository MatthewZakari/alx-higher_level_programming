#!/usr/bin/python3
j = 0
for i in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(i - j)), end="")
    i = 32 if i == 0 else 0
