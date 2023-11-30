#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    arglen = len(argv) - 1
    if arglen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sign = {'+': add, '-': sub, '*': mul, '/': div}
    if argv[2] in sign:
        a = int(argv[1])
        b = int(argv[3])
        sn = sign[argv[2]]
        res = sn(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
