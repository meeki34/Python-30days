# ducktype = Another way to Achieve Polymorphism
# Duck type = If it looks like a duck and quacks like a duck, it is a duck.

# "If it looks like a duck and quacks like a duck, it is a duck.
# 
# "

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Duck(Animal):
    def speak(self):
        print("quack")

class Car:
    alive = True
    def speak(self):
        print("Driving")
    
animals = [Dog(), Cat(), Duck(),Car()]

for animal in animals:
    animal.speak()
    print(f"{animal.alive}")