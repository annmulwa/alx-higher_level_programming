#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [rom[i] for i in roman_string] + [0]
    res = 0

    for j in range(len(num) - 1):
        if num[j] >= num[j + 1]:
            res += num[j]
        else:
            res -= num[j]
    return res
