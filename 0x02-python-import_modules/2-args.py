#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
