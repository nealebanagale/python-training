#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# [] - list are imutable
# () - tuple are not mutable

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1])  # access list elements
    print(game[1:5:2])  # same with range's start,stop,step\
    i = game.index('Paper')     # search
    game.append('Computer')
    game.insert(0, 'Computer')
    game.remove('Paper')        # omitted form list
    x = game.pop()              # removed last item and return the value
    print(i)
    print(x)
    del game[3]                 # delete statement by index
    print(', '.join(game))      # join string
    print(len(game))            # length
    print_list(game)

    # tuple
    game2 = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock')     # immutable
    print(game2)


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
