#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# {key: val} - dict

def main():
    # animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #            'giraffe': 'I am a giraffe!', 'dragon': 'rawr'}
    animals = dict(kitten='meow', puppy='ruff!', lion='grrr',
                   giraffe='I am a giraffe!', dragon='rawr')

    # Print keys
    for k in animals.keys():
        print(k)

    # Print values
    for v in animals.values():
        print(v)

    # Print elemet
    print(animals['lion'])

    # re-assign elements
    animals['lion'] = "RAWR"
    print(animals['lion'])

    # add new elements
    animals['monkey'] = 'banana'

    # search for a keys
    print('lion' in animals)
    print('found!' if 'lion' in animals else 'nope!')

    # key error
    # print(animals['godzilla'])  # exception
    print(animals.get('godzilla'))      # None value

    print_dict(animals)


def print_dict(o):
    for k, v in o.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
