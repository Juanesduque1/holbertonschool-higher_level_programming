#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print("{}".format(' '.join(map(str, line))))
