#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# List
# []
x = [1, 2, 3, 4, 5]
x[2] = 42    # mutable
for i in x:
    print('i is {}'.format(i))

# Tuple
# ()
t = (1, 2, 3, 4, 5)
# t[4] = 42   # imutable
for i in t:
    print('t is {}'.format(i))

# Range
r = range(5, 50, 5)     # start, end, step
for i in r:
    print('r is {}'.format(i))

r2 = list(range(5, 50, 5))
# r2[2] = 42  # immutable - requires list() wrapper
for i in r2:
    print('r2 is {}'.format(i))

# Dictionary
# searchable sequence of key value pairs
d = {'one': 1, 'two': 2}
d['two'] = 42   # mutable
for k, v in d.items():
    print('k: {}, v: {}'.format(k, v))
