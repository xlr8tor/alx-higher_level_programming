#!/usr/bin/python3
import sys

total = 0
for num in sys.argv[1:]:
    total += int(num)
print(f"{total:d}")
