#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[2])
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
