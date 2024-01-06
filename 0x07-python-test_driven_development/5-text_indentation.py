#!/usr/bin/python3
'''
Defines the text-indentation function
'''


def text_indentation(text):
    '''
    Print text with two new lines after each '.', '?', and ':'
    text must be a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cnt = 0
    while cnt < len(text) and text[cnt] == ' ':
        cnt += 1

    while cnt < len(text):
        print(text[cnt], end="")
        if text[cnt] == "\n" or text[cnt] in ".?:":
            if text[cnt] in ".?:":
                print("\n")
            cnt += 1
            while cnt < len(text) and text[cnt] == ' ':
                cnt += 1
            continue
        cnt += 1
