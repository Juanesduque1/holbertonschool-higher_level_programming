#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string) -1, -1, -1):
            result = roman_numbers[roman_string[i]]
            if 3 * result < sum: 
                sum = sum - result
            else: 
                sum = sum + result
    return sum
