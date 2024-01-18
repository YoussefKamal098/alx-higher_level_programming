#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    print("{} arguments:".format(argc))

    if argc == 0:
        exit()

    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
