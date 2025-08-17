import math

name = input("what is your name ")
age = int(input("what is ur age "))
height = float(input("what is ur height "))

print ("Hello" + name)
print ("You are eligable for this task"+  str(age))
print ("Yor height is validated in cm "+  str(height))

# number function()
pi = 3.14

x = 3
y = 4
c = 4

print(pi)
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,1))
print(math.sqrt(420))
print(max(x,y,c))

# slicing a create a substring by extracting elements from anther string 
#indexing[] or slice[]
# [start:stop:step]

name = "syed zahid"
reverse_name = "syed"

print(name[-1])
print(name[0])
print(name[0:4])
print(reverse_name[::-1])
print(name[::2])

website1 = "http://google.com"
website2 = "http://x.com"

slice = slice(7,-4)
print(website1[slice],website2[slice])