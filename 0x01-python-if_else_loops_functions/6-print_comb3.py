#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end="")
        print(", " if i != 99 else "", end="" if i != 99 else "\n")
