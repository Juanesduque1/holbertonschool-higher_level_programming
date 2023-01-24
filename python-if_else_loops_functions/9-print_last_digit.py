#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number) % 10
    print("{}".format(number), end='')
    return number
