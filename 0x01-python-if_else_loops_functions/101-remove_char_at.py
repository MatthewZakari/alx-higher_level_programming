#!/usr/bin/python3

def remove_char_at(s, n):
    # Check if n is a valid index
    if 0 <= n < len(s):
        # Create a cpy of the str with the char at position n removed
        return s[:n] + s[n+1:]
    else:
        # If n is out of bounds, return the original string
        return s
