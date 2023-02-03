#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0

    for num in my_list:
        numerator += num[0] * num[1]
        denominator += num[1]
    return numerator / denominator
