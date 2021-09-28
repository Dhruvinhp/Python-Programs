from abc import ABC, abstractmethod


class Shape(ABC):
    # Shape is parent class so with abstract method we can put required method to write necessary
    # in this, printarea must written in child class

    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    side = 4

    def __init__(self):
        self.length = 4
        self.width = 6

    def printarea(self):
        return self.length * self.width


rect1 = Rectangle()
# you can't create object of abstract class like, abc = shape()
print(rect1.printarea())
