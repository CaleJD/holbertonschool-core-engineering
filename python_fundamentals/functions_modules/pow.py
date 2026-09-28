#!/usr/bin/env python3

i = 0
def pow(a, b):
    result = 0
    while i < b:
        power = a
        result += a * power
        print(f"{result}")
        i = i + 1