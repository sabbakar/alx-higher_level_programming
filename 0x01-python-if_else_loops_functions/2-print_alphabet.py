#!/usr/bin/python3
def lowercaseAlphabet():
    alphabets = ""
    for c in range(97, 123):
        alphabets += chr(c)
    return alphabets


print("{}".format(lowercaseAlphabet())
