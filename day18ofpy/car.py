# object = A "Bundle" of related attributes and methods 
# Ex phone, cup, book;
# methods = A function that is defined inside a class
# function = A function that is defined outside a class
# object = A "Bundle" of related attributes and methods


# class = A is a Blueprint for creating objects
# object = A "Bundle" of related attributes and methods

from classs import Car

car1 = Car("BMW",2022,"black",True)
car2 = Car("Audi",2023,"red",False)
print(car1.model,end = " ")# we using the attriube of the acces operator 
print(car2.year)
print(car1.color)
print(car2.for_sale)


car2.drive()
car1.sell()
car2.describe()