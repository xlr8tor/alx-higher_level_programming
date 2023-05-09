#!/usr/bin/python3

def print_last_digit(number):
    absval = number * -1 if number < 0 else number
    unsigned_number = absval % 10
    print(unsigned_number, end="")
    return unsigned_number
