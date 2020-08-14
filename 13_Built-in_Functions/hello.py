#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'the number of bunnies is {self._n}'

    def __str__(self):
        return f'str: the number of bunnies is {self._n}'


s = Bunny(47)
print(repr(s))  # print the return of __repr__

x = Bunny(47)
print(x)
print(ascii(x))     # escape unicode value


# Containers
x = (1, 2, 3, 4, 5)
y = x
y2 = len(x)
y3 = reversed(x)
y4 = list(reversed(x))   # reversed obj string
y5 = sum(x)
y6 = sum(x, 10)
y7 = max(x)
y8 = min(x)
y9 = any(x)     # boolean function
y10 = all(x)    # boolean function
print(x)
print(y)
print(y2)
print(y3)
print(y4)
print(y5)
print(y6)
print(y7)
print(y8)
print(y9)
print(y10)

z = (6, 7, 8, 9, 10)
z1 = zip(x, z)
for a, b in z1:
    print(f'{a} - {b}')

n = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x):   # enumerate - gives index and a value,
    print(f'{i}: {v}')


# Object and class functions
a = 42
b = type(a)
b1 = isinstance(a, int)
b2 = id(a)
print(a)
print(b)
print(b1)
print(b2)
