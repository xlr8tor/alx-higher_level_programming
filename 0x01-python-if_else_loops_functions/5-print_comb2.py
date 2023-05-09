#!/usr/bin/python3

for i in range(100):
    print("{dec:02d}".format(dec=i), end=", " if i < 99 else "\n")
