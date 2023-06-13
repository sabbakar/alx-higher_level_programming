#!/usr/bin/python3
def lowercaseAlphabets():
    alphabets = ""
    for c in range(97, 123):
        alphabets += chr(c)
    return alphabets

print(lowercaseAlphabets())
