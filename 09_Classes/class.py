#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# class is the basis of all data in Python
# everything is an object in Python, and a class is how an object is defined.

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):    # self - reference to the object !class
        print(self.sound)

    def move(self):     # self - reference to the object !class
        print(self.movement)


def main():
    donald = Duck()
    donald.quack()
    donald.move()


if __name__ == '__main__':
    main()
