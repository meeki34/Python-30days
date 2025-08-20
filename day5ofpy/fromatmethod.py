# str format = optional method atha gives users more control 
     # when displaying output

animal = "cat"
item = "fish"

# {} this are a placeholder for the variables 

# print("The {} chased the {}.".format(animal, item))
# print("The {} chased the {}.".format(item, animal))# positional arguments
# print("The {1} chased the {0}.".format(item, animal))
# print("The {animal} chased the {item}.".format(animal="dog", item="cat"))
# keyword arguments

# print("The {animal} chased the {animal}".format(animal="cat", item="person"))

""" text = "The {animal} chased the {item}."
print(text.format(animal="cat", item="fish")) """


# name = "syed"

""" print("Hello, my name is: {}".format(name)) 
print(f"Hello, my name is: {name:>10}. nice to me you ".format(name)) # right align
print("Hello, my name is: {:<10}".format(name)) # left align
print("Hello, my name is: {:^10}".format(name)) # center align
print("Hello, my name is: {:=^10}".format(name)) # center align and fill with = """

import math

number = 3.14159
num = 1000

print("The number pi is {:.3f}".format(number))
print("The Number is  {:,}".format(num))
print("The number is {:b}".format(num))# this an binary represent 
print("The number pi {:o}".format(num))
print("The number is {:x}".format(num))
print("The number is {:E}".format(num))
