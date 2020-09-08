
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"    # attribute
        self.name = "Class A"  # same attribute


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"    # attribute
        self.name = "Class bug"     # same attribute


class C(A, B):              # inherits multiple class
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name)    # prints Class A because of method resolution order

# method resolution order - starts in the current class (Class C)
#                         - thenlooks in the superclasses in the order
#                        - defined from left to right (Class A is listed first)


c = C()
c.showProps()
# inspect method resolution order
print(C.__mro__)
