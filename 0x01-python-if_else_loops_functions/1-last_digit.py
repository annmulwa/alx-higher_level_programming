#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -(num)
output = "Last digit of {} is {}".format(number, num)
if num > 5:
    print(f"{output} and is greater than 5")
elif num == 0:
    print(f"{output} and is 0")
elif num < 6 and num != 0:
    print(f"{output} and is less than 6 and not 0")
