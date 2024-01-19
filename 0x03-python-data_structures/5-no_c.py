#!/usr/bin/python3
def no_c(my_string):
    strcpy = ""

    for char in my_string:
        if char not in "cC":
            strcpy += char

    return strcpy
