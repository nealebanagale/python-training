#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#  loop uses a sequence
# use an iterator or list, tuple, or other collection type to control the loop
# The body of the loop is executed for each item in the sequence
# When the sequence is exhausted the loop ends.

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog':
        continue
    if pet == 'velociraptor':
        break
    print(pet)
else:
    print('that is all of the animals')
# for pet in range(5):
#     print(pet)
