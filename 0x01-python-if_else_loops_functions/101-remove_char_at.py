#!/usr/bin/python3
def remove_char_at(str, n):
    strcp = ''
    i = 0
    for a in str:
        if i != n:
            strcp = strcp + str[i]
        i = i + 1
    return (strcp)
