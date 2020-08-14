#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class RevStr(str):  # inherit from standard String class
    def __str__(self):  # overidding str method
        return self[::-1]


def main():
    hello = RevStr('Hello, World.')
    print(hello)


if __name__ == '__main__':
    main()
