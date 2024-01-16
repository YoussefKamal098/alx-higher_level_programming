#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print(f"{ord(char) - 32:c}", end="")
        else:
            print(char, end="")
