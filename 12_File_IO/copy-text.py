#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('.\\Chap12\\lines.txt', 'rt')  # read-text mode
    outfile = open('.\\Chap12\\lines-copy.txt', 'wt')    # write-text mode
    for line in infile:
        outfile.writelines(line)
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()     # prevent data loss
    # infile.close()    #closed in main file
    print('\ndone.')


if __name__ == '__main__':
    main()
