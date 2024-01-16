#!/usr/bin/python3
def uppercase(str):
    for char in str:
        lower = ord('a') <= ord(char) <= ord('z')
        print("{:c}".format(ord(char) - 32 if lower else ord(char)), end="")

    print()
