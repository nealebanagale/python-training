#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# default, it opens the file in read-only mode
# 'r' - read-only
# 'w' - write mode: and if you open in write mode,
#       it empties the file if the file is not empty,
#       and it starts at the beginning and writes over the file.
#        If the file doesn't exist, it creates it.
# 'a' - a pen mode, this is just like write,
#       but if the file already has some content in it,
#       it starts at the end of the file and it does not empty the file
#       and it does not create the file.
# '+ - optional plus, <mode>+, which will allow you to both read and write.
# 'b'/'t' -  binary or text mode (default text mode)

def main():
    # open() - open file in python
    f = open('.\\Chap12\\lines.txt', 'r+t')    # file object
    for line in f:
        print(line.rstrip())            # rstrip:strip white spaces & new line


if __name__ == '__main__':
    main()
