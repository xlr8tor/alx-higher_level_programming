#!/usr/bin/python3

for i in "abcdefghijklmnopqrstuvwxyz":
    if i != "e" and i != "q":
        print("{char}".format(char=i), end="")
