#!/usr/bin/env python3

def print_last_digit(number):
    result = abs(number) % 10
    if number < 0:
        number = -number
    print("{}".format(result), end='')
    return result
