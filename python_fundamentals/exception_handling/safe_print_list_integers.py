#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x + 1):
        try:
            print("{:d}".format(my_list[i]))
            count += 1
        except (TypeError, ValueError):
            pass
    return count
