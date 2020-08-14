#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# statement = a unit of execution
# ex; import statement
# 1 statement per line

# expression = a unit of evaluation
# ex: x = y/(x , y)/f()
import platform

version = platform.python_version()

print('This is python version {}'.format(version))
print('hello')  # a statement
