#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arglen = len(argv) - 1

    if arglen == 0:
        print("{} arguments.".format(arglen))
    elif arglen == 1:
        print("{} argument:".format(arglen))
        print("{}: {}".format(arglen, argv[1]))
    elif arglen > 1:
        print("{} arguments:".format(arglen))
        for i in range(1, arglen + 1):
            print("{}: {}".format(i, argv[i]))
