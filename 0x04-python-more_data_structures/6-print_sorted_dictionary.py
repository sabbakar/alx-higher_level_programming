#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print(key + ":", a_dictionary[key])
