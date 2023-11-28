#!/usr/bin/python3
def uppercase(str):
    for i in str:
        tmp = i
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(tmp) - 32)
        print("{}".format(tmp), end='')
    print()
