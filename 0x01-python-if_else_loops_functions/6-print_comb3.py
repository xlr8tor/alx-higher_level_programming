#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        print("{d}{e}".format(d=i, e=j), end=", " if i < 8 else "\n")
