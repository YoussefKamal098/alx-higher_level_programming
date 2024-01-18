#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{} arguments:".format(len(sys.argv)))
    for i in range(len(sys.argv)):
        print("{}: {}".format(i + 1, sys.argv[i]))
