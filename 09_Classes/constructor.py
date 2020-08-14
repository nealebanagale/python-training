#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# An object is an instance of a class
# An object is created by calling the class as if it were a function
# And the constructor is used to initialize the object

class Animal:
    # class constructor - initializer
    # def __init__(self, type, name, sound):  # method and has self
    def __init__(self, **kwargs):  # method and has self
        # _ in the beggining of the name/ not to access directly
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'type' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'type' in kwargs else 'rawr'

    # accecssors / getters
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'
          .format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
    print_animal(Animal())  # default object


if __name__ == '__main__':
    main()
