#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = '''This is a long
 string with a     bunch of words in it.'''
print(s)
print(s.split())    # list of words/ removes whitespaces before split
print(s.split('i'))    # split on 'i'

# join with parameters
l2 = s.split()
s2 = ':'.join(l2)
print(s2)
