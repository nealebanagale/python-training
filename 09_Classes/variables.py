#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # class variable
    # not defined in a method
    # x = [1, 2, 3]

    def __init__(self, **kwargs):
        # object variables
        # They only exist, when the object is created from the class
        # they do not exist in the class itself
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    # Encapsulation is one of the major benefits of object oriented programing.
    # If my variables are encapsulated, that means that they belong to
    # the object and not to the class.
    def type(self, t=None):
        if t:
            self._type = t  # set

        return self._type   # get

    def name(self, n=None):
        if n:
            self._name = n

        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s

        return self._sound

    def __str__(self):
        # users getter
        return f'{self.type()} is named "{self.name()}"says "{self.sound()}".'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print(a0)
    print(a1)

    # Object variables
    # they don't exist in the class
    # bound to the object, not to the class itself
    a0._name = 'Joe'
    print(a0._name)

    # print(a0.x)
    # a1.x[0] = 7     # x variable is not encapsulated and so it exists
    # print(a0.x)


if __name__ == '__main__':
    main()
