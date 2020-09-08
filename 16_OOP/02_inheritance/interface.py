from abc import ABC, abstractmethod
# interface - kind of promise
# class makes promise/contract to provide certain kind of behavior/capability


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


# combination of multiple inheritance to implement inheritance
class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):   # interface
        return f"{{\"circle\" :{str(self.calcArea())}}}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
