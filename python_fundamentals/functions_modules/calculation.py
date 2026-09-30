#!/usr/bin/env python3

from calculator_1 import (add, sub, mul, div)

a = 10
b = 5
res = 0
calcs = [
    (add, "+"),
    (sub, "-"),
    (mul, "*"),
    (div, "/")
    ]
if __name__ == "__main__":
    for calc, symbol in calcs:
        res = calc(a, b)
        print("{} {} {} = {}".format(a, symbol, b, res))
