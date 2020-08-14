#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from decimal import Decimal

x = 7
y = 7.0
s = 'seven'.upper()    # string is an object
# multi-line string
s2 = '''
    seven
'''
s3 = 'seven {} {}'.format(8, 9)    # placeholders are positional arg
s4 = 'seven {1} {0}'.format(8, 9)    # swap
s5 = 'seven "{1:<09}" "{0:>9}"'.format(8, 9)    # : w/ spaces / 0 fill
sa = 8
sb = 9
s6 = f'seven {sa} {sb}'  # f string (only 3.6 up)

b = True
n = None
print('x is {}'.format(x))
print(s)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
# Python uses dynamic typing
# duck typing - type of a value is determined by the value itself
# if it walks like a duck, it's a duck
print(type(x))
print(type(y))
print(type(s))
print(type(b))
print(type(n))  # NoneType

# Integers and Floats

ix = 7 / 3
ix2 = 7 // 3     # // - disregard remainder
ix3 = 7 % 3      # % - modulo
ix4 = .1 + .1 + .1 - .3     # floating point arithmetic
ia = Decimal('.10')
ib = Decimal('.30')
ix5 = ia + ia + ia - ib
print('ix is {}'.format(ix))
print(type(ix))
print('ix2 is {}'.format(ix2))
print(type(ix2))
print('ix3 is {}'.format(ix3))
print(type(ix3))
print('ix4 is {}'.format(ix4))
print(type(ix4))
print('ix5 is {}'.format(ix5))
print(type(ix5))


# Bool Types
bb = 7 > 5      # comparison operator returns Bool type
bn = None       # None type - used to represent absence of a value
print('x is {}'.format(bb))
print(type(bb))
print('bn is {}'.format(bn))
print(type(bn))

if bn:
    print("True")
else:
    print("False")  # None evaluates false


# Types and Id
tx = (1, 'two', 3.0, [4, 'four'], 5)     # Tuple
ty = (1, 'two', 3.0, [4, 'four'], 5)
print('t is {}'.format(bb))
print(type(tx))
print(type(ty))
print(type(tx[2]))   # inspect element in structure

# unique ID for object
print(id(tx))
print(id(ty))
if tx is ty:
    print("yep")
else:
    print("nope")

# two different objects for the literal number one
print(id(tx[0]))
print(id(ty[0]))

if tx[0] is ty[0]:
    print("yep")
else:
    print("nope")

if isinstance(tx, tuple):
    print("tuple")
else:
    print("not tuple")

tyl = [1, 'two', 3.0, [4, 'four'], 5]

if isinstance(tyl, tuple):
    print("tuple")
elif isinstance(tyl, list):
    print("list")
else:
    print("not tuple")
