#!/usr/bin/python3

def print_last_digit(number):
    print("{}".format(number), end='')
    return abs(number) % 10
