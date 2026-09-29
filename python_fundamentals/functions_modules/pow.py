#!/usr/bin/env python3

def pow(a, b):
    i = 1
    result = 0
    if b < 0:
        b = abs(b)
        result = 0
        while i < b:
            power = a
            result += a * power
            i = i + 1
        result = 1 / result
        return result
    else:
        while i < b:
            power = a
            result += a * power
            i = i + 1
        return result
