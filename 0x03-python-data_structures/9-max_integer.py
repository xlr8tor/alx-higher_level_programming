#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    maxn = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maxn:
            maxn = my_list[i]
    return maxn
