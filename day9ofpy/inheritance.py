# # inheritance
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def show(self):
# #         print(self.name, self.age)
# #
# # class Employee(Person):
# #     def __init__(self, name, age, salary):
# #         super().__init__(name, age)
# #         self.salary = salary
# #
# #     def show(self):
# #         print(self.name, self.age, self.salary)
# #
# # e = Employee("John", 25, 50000)
# # e.show()

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def show(self):
        print(self.firstname, self.lastname)

x = Person("BALA","ARUN")
y = Person("RAM","KUMAR")
z = Person("RAJA","MOHAN")
u = Person("KUMAR","SURESH")
x.show()