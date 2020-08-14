#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = 112
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 2')

print('something else')
# blocks does not define scope in python
print('z is {}'.format(z))
# functions, objects, and modules do define scope
