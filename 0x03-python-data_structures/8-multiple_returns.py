#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if len(sentence) == 0:
        first = None
        return first
    else:
        return length, first
        print("{:d} {}".format(length, first))
        
