#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print(char, end="")
