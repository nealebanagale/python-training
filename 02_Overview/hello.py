#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
print('Hello, World.')  # with literal string

# string object it self
print('Hello, World. {}' .format(x))  # '{}' - placeholder
print(f'Hello, World. {x}')   # f string - stands for format()
print('Hello, World. %d' % x)    # %d - placeholder integer
