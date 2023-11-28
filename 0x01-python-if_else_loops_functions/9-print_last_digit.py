#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    lastnum = number % 10
    print("{}".format(lastnum), end="")
    return (lastnum)
