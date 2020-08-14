#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Strings are first class object
print('Hello, World. {}'.format(42 * 7))
print("""
    Hello, World. {}'
""".format(42 * 7))

s = 'Hello, World. {}'
print(s.format(42 * 7))


# Subclass string
class MyString(str):    # str - string clas
    def __str__(self):
        return self[::-1]


b = MyString('Hello, World.')
print(b)


# Common string methods
# String is immutable
print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())     # capitalizes just the first letter
print('Hello, World.'.title())  # capitalizes the first letter of every word
print('Hello, World.'.swapcase())   # swap the case of every letter
print('Hello, World.'.casefold())   # remove case distinctions
s1 = 'Hello, World.'
s2 = s1.upper()
print(id(s1))
print(id(s2))   # returns a new object

s3 = 'this is another string'
print(s1 + ' ' + s3)  # concatenate

s4 = 'this string ' 'that string'    # concat string literals
print(s4)


# Formatting strings
x = 42
y = 73
# {} - placeholders
print('the number is {bb} {xx}'.format(xx=x, bb=y))

# positional arguments
print('the number is {0} {1} {0}'.format(x, y))

# formatting instructions
# positional argument
print('the number is {0:<5} {1:>5} {1:+5}'.format(x, y))
t = 42 * 747 * 1000
print('the number is {:,}'.format(t))     # format comma
print('the number is {:,}'.format(t).replace(',', '.'))  # replace
print('the number is {:.3f}'.format(t))     # specify decimal
z = 42
print('the number is {:x}'.format(z))     # hexadecimal
print('the number is {:o}'.format(z))     # octadecimal
print('the number is {:b}'.format(z))     # binary

# f string formatting for python > 3.6
n = 42
print(f'the number is {x:.3f}')     # formatting will work
