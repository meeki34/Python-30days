# matrix 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(matrix)   

class MyClass:# create a class named MyClass
    x = 5

myObj = MyClass() # create an object of MyClass
print(myObj.x)

# thE __init__() Function

class Person1:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
p1 = Person1("John",36)
p2 = Person1('Ramesh',21)
print(p1.name)
print(p1.age)
print(p2.name,p2.age)


# --str--()

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

p3 = Person("John",36)
print(p3)#The string respresentation of an object without the  __str__()
# methd:
print(p3.__str__())


class Persons:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
p4 = Persons("John",36)
print(p4) #The string respresentation of an object with the  __str__()

# self parameter
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

class students:
    def __init__(mysillyobject, name,age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)
            
p5 = students("John",36)
p5.myfunc()

# Modify object properties 
p1.age = 40
del p1