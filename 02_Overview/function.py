#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n=1):
    print(n)
    return n * 2


function(47)
function()
x = function(42)    # all functions returns a value
print(x)
# default value of none - absence of a value
