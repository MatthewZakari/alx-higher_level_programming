#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return [name for name in dir(obj) if not callable(getattr(obj, name)) and not name.startswith('__')]
