#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1():
    print('this is f1')


def f2():
    def f3():
        print('this is f3')
    return f3


x = f1  # assign object func to variable
x()     # execute variable with object func
x2 = f2()
x2()
# f3()    # cannot call directly - exist in scope of f2


def f(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2


@f  # decorator? wrapped in f function
def f4():
    print('this is f4')


# f4 = f(f4)
# f4()
f4()    # no more assignment wrapper
