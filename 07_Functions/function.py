#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = 5
    kitten(5, 6)     # arguments
    print(x)    # func alwasys returns a value (NONE val)
    a = 5
    print(id(a))
    kit(a)  # call by value
    print(f'in main: a is {a}')
    x2 = [5]
    kitten2(x2)
    print(f'in main: x2 is {x2}')


def kitten(a, b, c=1):    # default argument, must be in the end
    print('Meow.')
    print(a, b, c)


def kit(a):
    print(id(a))
    # function operates on a copy of the variable
    a = 3   # will not change in main()
    print(id(a))    # different id
    print('Meow.')
    print(a)


def kitten2(a):
    a[0] = 3    # called by reference (will object in element)
    print('Meow.')
    print(a)


# not imported, this is the main file
if __name__ == '__main__':
    main()
