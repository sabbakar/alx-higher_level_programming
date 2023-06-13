#!/usr/bin/python3
def lowercaseAlphabets():
    alphabets = ""
    for c in range(97, 123):
        if chr(c) not in ('q', 'e'):
        alphabets += chr(c)
    return alphabets


print("{}".format(
    lowercaseAlphabets()
), end="")
