#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = ('meow', 'grrr', 'purr')
    kitten(*x)  # call with a prepared list


def kitten(*args):  # * - variable length argument list
    if len(args):   # tuple
        for s in args:
            print(s)
    else:
        print('Meow.')


if __name__ == '__main__':
    main()
