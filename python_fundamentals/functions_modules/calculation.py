#!/usr/bin/env python3

from calculator_1 import (add, sub, mul, div)

a = 10
b = 5
res = 0
calcs = [add, sub, mul, div]
if __name__ == "__main__":
    for i in calcs:
        res = i(a, b)
        print("{}".format(res))
