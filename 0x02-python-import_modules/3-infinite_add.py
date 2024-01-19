#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    int_sum = 0
    for i in range(len(sys.argv) - 1):
        int_sum += int(sys.argv[i + 1])

    print(int_sum)
