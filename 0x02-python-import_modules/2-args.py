#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    if num_arguments == 1:
        print(num_arguments, " argument:")
        print("1:", arguments[0])

    elif num_arguments == 0:
        print(num_arguments, " arguments.")

    else:
        print(num_arguments, " arguments:")
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
