#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Combine the two sets using the union operator
    combined_set = set_1.union(set_2)

    # Cal the symmetric diff to get elements present in only one set
    only_diff_set = combined_set - (set_1.intersection(set_2))

    return only_diff_set
