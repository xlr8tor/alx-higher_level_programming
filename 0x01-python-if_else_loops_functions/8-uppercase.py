#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for c in str:
        c = ord(c)

        if c > 96 and c < 123:
            newstr += chr(c - 32)
        else:
            newstr += chr(c)
    print(newstr)
