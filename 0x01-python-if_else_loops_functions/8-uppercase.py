#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) - 32 if ord('a') <= ord(char) <= ord('z') else ord(char)), end="")

    print()
