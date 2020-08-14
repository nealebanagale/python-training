#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('.\\Chap12\\berlin.jpg', 'rb')    # b - read as binary
    outfile = open('.\\Chap12\\berlin-copy.jpg', 'wb')  # b

    # run continues
    while True:
        # buffer size (choose carefully)
        buf = infile.read(10240)    # 10k bytes
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)  # flush - flush buffer
        else:   # empty buffer
            break
    outfile.close()     # prevent data loss due to buffering
    print('\ndone.')


if __name__ == '__main__':
    main()
