#!/usr/bin/python3
def sumarg(argv):
    sum = 0
    arglen = len(argv) - 1
    if arglen == 0:
        print("{:d}".format(arglen))
        return
    else:
        s = 1
        while s <= arglen:
            sum += int(argv[s])
            s += 1
        print("{:d}".format(sum))

if __name__ == "__main__":
    import sys
    sumarg(sys.argv)
