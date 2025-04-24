from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self):
        pass


class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print(f'红色的{shape.name}')


class Green(Color):
    def paint(self, shape):
        print(f'绿色的{shape.name}')


shape = Rectangle(Red())
shape.draw()
