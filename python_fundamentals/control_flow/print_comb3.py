#!/usr/bin/env python3

first = 0
second = 0
for first in range(10):
    for second in range(first + 1, 10):
        print("{}{}".format(first, second), end='')
        print("\n" if (first, second) == (8, 9) else ", ", end='')
