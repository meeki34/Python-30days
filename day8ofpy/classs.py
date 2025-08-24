# Class and Object Relationship
# Class: Car (Blueprint)
# Attributes: color, model

# Methods: drive(), stop()

# ↓ Creates
# Object 1
# Car: Red Toyota

# drive(): "Red Toyota is driving!"

# Object 2
# Car: Blue Honda

# drive(): "Blue Honda is driving!"

# Object 3
# Car: Black Ford

# drive(): "Black Ford is driving!"

# Why is a Class Called a Blueprint?
# A class is like a blueprint or template that defines the structure (attributes) and behavior (methods) of objects. In this example, the Car class defines attributes like color and model, and methods like drive() and stop().

# An object is an instance of the class, created based on the blueprint. Each object has its own specific values for the attributes defined in the class. For example, Object 1 is a Red Toyota, Object 2 is a Blue Honda, and Object 3 is a Black Ford, all created from the same Car class blueprint.


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.speed = 0
    def drive(self):
        self.speed = 60
        return f"{self.color} {self.model} is driving at {self.speed} km/h."
    def stop(self):
        self.speed = 0
        return f"{self.color} {self.model} has stopped."
# Creating objects (instances) of the Car class
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")
car3 = Car("Black", "Ford")
# Using the methods of the Car class
print(car1.drive())  # Output: Red Toyota is driving at 60 km/h.
print(car2.drive())  # Output: Blue Honda is driving at 60 km/h.
print(car3.stop())   # Output: Black Ford has stopped.
print(car1.stop())   # Output: Red Toyota has stopped.
print(car2.stop())   # Output: Blue Honda has stopped.
print(car3.drive())  # Output: Black Ford is driving at 60 km/h.