#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys


def main():
    try:
        x = 5 / 0
    except ValueError:
        print('I cant a ValueError')
    except ZeroDivisionError:
        print(f'dont\'t divide by zero: {sys.exc_info()[1]}')
    else:
        print('good job')
        print(x)


if __name__ == '__main__':
    main()
