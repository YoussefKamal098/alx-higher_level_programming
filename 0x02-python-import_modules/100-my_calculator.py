#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    a = sys.argv[1]
    b = sys.argv[2]
    func = None

    if sys.argv[3] == '+':
        func = add
    elif sys.argv[3] == '-':
        func = sub
    elif sys.argv[3] == '*':
        func = mul
    elif sys.argv[3] == '/':
        func = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, sys.argv[3], b, func(a, b)))
