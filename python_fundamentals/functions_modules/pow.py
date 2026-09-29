#!/usr/bin/env python3

def pow(a, b):
    i = 0
    result = 0
    while i < b:
        power = a
        result += a * power
        print(f"{result}")
        i = i + 1
