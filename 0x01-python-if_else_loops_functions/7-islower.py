#!/usr/bin/python3

def islower(c):
    if c.islower():
        return (True)
    else:
        return (False)
    print("'' => {}".format("lower" if islower("") else "upper"))
