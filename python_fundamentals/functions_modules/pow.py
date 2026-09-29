#!/usr/bin/env python3

def pow(a, b):
    result = 0
    if b < 0:
        b = abs(b)
        for i in range(b):
            result *= a
        result = 1 / result
        return result
    else:
        for i in range(b):
            result *= a
        return result
