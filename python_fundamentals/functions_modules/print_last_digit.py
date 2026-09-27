#!/usr/bin/env python3

def print_last_digit(number):
    result = number % 10
    print("{}".format(result), end = '')
    return result
