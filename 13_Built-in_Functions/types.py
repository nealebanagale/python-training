#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'    # literal string
y = int(x)  # int - returns int from another type

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

x2 = -47.3
y2 = abs(x2)  # absolute
print(f'y2 is {type(y2)}')
print(f'y2 is {y2}')


# divmode
x3 = 47
y3 = divmod(x3, 3)  # retrns tuple
print(f'y3 is {type(y3)}')
print(f'y3 is {y3}')


# complex
x4 = 47
y4 = complex(x4, 3)  # retrns tuple
print(f'y4 is {type(y4)}')
print(f'y4 is {y4}')
