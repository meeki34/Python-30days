#super() is used to call the method of parent class
# = functioon used in a child class to call a method of parent class {super class}
#super() is a built-in function that returns a temporary object of a superclass
#which allows us to call a method of a parent class.
#The object returned by the super() function can be assigned to a variable
#and then used to call a method of a parent class.

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f" It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, radius,color,is_filled):
        super().__init__(color, is_filled)
        self.radius = radius
        

class Square(Shape):
    def __init__(self, width,color,is_filled):
        super().__init__(color, is_filled)
        self.width = width
       
    

class Triangle(Shape):
    def __init__(self, width,height,color,is_filled):
        super().__init__(color,is_filled)
        self.height = height
        self.width = width
        

circle = Circle(10,"red",True)
print(circle.radius)
print(circle.color)
print(circle.is_filled)
print(circle.__dict__)

square = Square(10,"red",True)
square.describe()
print(f"{circle.radius} is radius of circle")

Triangle = Triangle(10,20,"red",True)
Triangle.describe()
print(Triangle.width)
print(Triangle.height)
print(Triangle.color)
print(Triangle.is_filled)
print(Triangle.__dict__)

square = Square(10,"red",True)
square.describe()
print(square.width)
print(square.color)
print(square.is_filled)
print(square.__dict__)
