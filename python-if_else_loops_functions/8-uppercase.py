#!/usr/bin/python3


def uppercase(str):
    string = ''
    for i in str:
        n = ord(i)
        if n >= 97 and n <= 122:
            n = n - 32
        string += chr(n)
    print("{}".format(string))
