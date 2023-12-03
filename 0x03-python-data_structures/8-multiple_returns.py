#!/usr/bin/python3
def multiple_returns(sentence):
    tuplen = len(sentence)
    ch_0 = sentence[0] if tuplen > 0 else "None"
    tupl = tuplen, ch_0
    return (tupl)
