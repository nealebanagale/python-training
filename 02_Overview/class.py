#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# class = a definition
# object = an instance of a class.

class Duck:
    # class properties
    sound = 'Quack'
    walking = 'Walks like a duck.'

    # first argument for a method inside of a class is always 'self'
    # self - reference to the object when the class is used to create an object
    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    donald = Duck()     # donald is now object of class Duck()
    donald.quack()
    donald.walk()


if __name__ == '__main__':
    main()
