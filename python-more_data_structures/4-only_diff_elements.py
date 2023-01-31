#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result1 = set_1.difference(set_2)
    result2 = set_2.difference(set_1)
    result = result1.union(result2)
    return result
