#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    # Get the names defined in the module
    names = dir(hidden_4)

    # Sort the names in alphabetical order
    names.sort()

    # Loop through the names
    for name in names:
        # Check if the name does not start with __
        if not name.startswith("__"):
            # Print the name
            print(name)
