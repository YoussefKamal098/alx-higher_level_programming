#!/usr/bin/python3
for char in reversed(range(ord('a'), ord('z') + 1)):
    print("{:c}".format(char - 32 if char % 2 != 0 else char), end="")
