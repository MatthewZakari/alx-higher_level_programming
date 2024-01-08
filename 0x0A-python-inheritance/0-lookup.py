#!/usr/bin/python3

def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return [name for name in dir(obj) if not name.startswith('__')]
