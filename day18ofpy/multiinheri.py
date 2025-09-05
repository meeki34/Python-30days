# multiple inheritance 
class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name}eating")

    def sleep(self):
        print(f"{self.name}sleeping")



class prey1:
    def flee(self):
        print("fleeing")

class predator:
    def hunt(self):
        print("hunting")

class Rabbit(prey1, predator,Animal):
    def jump(self):
        print("jumping")

class Hawk(predator, prey1, Animal):
    def swim(self):
        print("swimming")



class fish(prey1, predator):
    pass

rabbit = Rabbit("rabbit")
rabbit.eat()
rabbit.sleep()
rabbit.flee()
rabbit.jump()   


