#!/usr/bin/python3
for i in range(0, 100):
    if i in [99]:
        print("{}".format(i))
    print("{:02d}".format(i), end=", ")
