#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A function that is associated with a class is called a method

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    # setter/getter
    def type(self, t=None):
        if t:
            self._type = t

        return self._type

    def name(self, n=None):
        if n:
            self._name = n

        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s

        return self._sound

    # specially named method
    # string representation of object
    def __str__(self):
        return f'{self.type()} is named "{self.name()}" says "{self.sound()}".'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    a0.sound('bark')
    print(a0)
    print(a1)


if __name__ == '__main__':
    main()
