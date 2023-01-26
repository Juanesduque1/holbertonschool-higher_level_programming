#!/usr/bin/python3

import sys


def infinite_addition():

    length = len(sys.argv)
    add = 0
    for i in range(1, length):
        add += int(sys.argv[i])
    print(add)


if __name__ == "__main__":
    infinite_addition()
