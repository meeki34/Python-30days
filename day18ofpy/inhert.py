# inheritance = Allow a class to inhert attribute and methods from another class 
# Helps with code reusabitly and extensibility 
# class child(parent)

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
   def speak(self):
        print(f"{self.name} is barking")
   pass
 

class Cat(Animal):
   def speak(self):
        print(f"{self.name} is meowing")
   pass
    
class Mouse(Animal):
    def speak(self):
        print(f"{self.name} is squeaking")
    pass

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("jerry")

print(dog.name)
print(cat.name)
print(mouse.name)

mouse.eat()# we are called the method
mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()

print(dog.is_alive)
print(cat.is_alive)
print(mouse.is_alive)