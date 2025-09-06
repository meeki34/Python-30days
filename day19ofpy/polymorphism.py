# Polymorphism  = it mean to have many forms or faces
#                   poly = many
#                   morph = forms
#                   polymorphism = many forms

#  two ways to achieve polymorphism
#  1. method overloading
#  2. method overriding

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base # this an width of triangle
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping = topping
        self.radius = radius

shapes = [Circle(4), Square(5), Triangle(6,7),Pizza("cheese",10)]# list of objects


for shape in shapes:
    print(f"{shape.area()}cm")