#!/usr/bin/python3
def uniq_add(my_list=[]):
    return reduce(lambda c, x: c + x, set(my_list))
