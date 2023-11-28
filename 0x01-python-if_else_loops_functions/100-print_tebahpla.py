#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    if 'a' <= chr(i) <= 'z' or 'A' <= chr(i) <= 'Z':
        print(chr(i) if i % 2 == 0 else chr(i - 32), end="")
