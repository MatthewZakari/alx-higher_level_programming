#!/usr/bin/python3

for i in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(
        chr(i) if ('a' <= chr(i) <= 'z' or 'A' <= chr(i) <= 'Z')
        and i % 2 == 0 else ""), end="")
