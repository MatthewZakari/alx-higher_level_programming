#!/usr/bin/env python3
def uppercase(s):
    print("".join(
        chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        for char in s))
