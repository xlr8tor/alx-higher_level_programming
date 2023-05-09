#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

mod = abs(number) % 10
mod = -mod if (number < 0) else mod
print(f"Last digit of {number:d} is {mod}", end=" ")
if (mod > 5):
    print("and is greater than 5")
elif (mod == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
