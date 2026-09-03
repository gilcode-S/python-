from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass


class Cicle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Cicle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings
        


shapes = [Cicle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 16)]

# loop to display all shapes

for shape in shapes:
    print(shape.area())
