#!/usr/bin/python3
for i in range(0, 100):
    print("{:02d}".format(i), end="")
    print(", " if i != 99 else "", end="" if i != 99 else "\n")
