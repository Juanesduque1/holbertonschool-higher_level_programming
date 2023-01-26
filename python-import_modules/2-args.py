#!/usr/bin/python3

import sys


def print_args():

    length = (len(sys.argv))

    if length == 1:
        print("0 arguments.")
        return
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
        return
    elif length > 2:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            value = str(sys.argv[i])
            print("{}: {}".format(i, value))
        return


if __name__ == "__main__":
    print_args()
