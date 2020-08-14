#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform


def main():
    message()   # delimited by indention


def message():
    print('This is python version {}'.format(platform.python_version()))
    print('line 2')
    if False:
        print('line 3')
    else:
        print('not true')


if __name__ == '__main__':  # conditional statement
    main()
