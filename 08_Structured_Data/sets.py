#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# set is like a list that does not allow duplicate element
# used for checking membership of a set

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    print_set(a - b)    # a not in b
    print_set(a | b)    # in a or b
    print_set(a ^ b)    # a or b but not both
    print_set(a & b)    # members in both


def print_set(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


if __name__ == '__main__':
    main()
