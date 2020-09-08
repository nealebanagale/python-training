from abc import ABC, abstractmethod
# ABC - Abstract Base Class
# Abstract - intended to be a blueprint
#          - subclasses to provide concrete implementations
#          - enforce the constraint that subclasses have to implement


# Base class
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod     # tells python to override from subclasses
    def calcArea(self):
        pass


# sub classes
class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape()    # abstract classes cannot be instantiated
c = Circle(10)
print(c.calcArea())
s = Square(25)
print(s.calcArea())
