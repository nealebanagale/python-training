#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys      # module import
import os
import random
import datetime
# doc.python.org/library


def main():
    v = sys.version_info
    v2 = sys.platform
    o = os.name
    o2 = os.getenv('PATH')
    o3 = os.getcwd()
    o4 = os.urandom(25).hex()   # 25 bytes on hexadecimal

    print('Python version {}.{}.{}'.format(*v))
    print(v2)
    print(o)
    print(o2)
    print(o3)
    print(o4)

    # Random
    p = random.randint(1, 1000)
    print(p)

    it = list(range(25))
    print(it)
    random.shuffle(it)
    print(it)

    # datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.minute)
    print(now.second)
    print(now.microsecond)


if __name__ == '__main__':
    main()
