#!/usr/bin/python3

import hidden_4


if __name__ == "__main__":

    directory = dir(hidden_4)

    for i in range(len(directory)):
        if directory[i][1] != "_":
            print(directory[i])
