# this an repeatetion of what we learn for passed by 5 day

# we learn to declare an variable

name = "Syed zahid"
age = 21
print(name)
print(age)

# we use the math operation 

# addition
print(5 + 5)
# subtraction
print(10 - 5)
# multiplication
print(5 * 5)
# division
print(10 / 5)
# exponentiation
print(5 ** 2)
# floor division
print(10 // 3)
# modulus
print(10 % 3)

# we learn condition statement

if statement := True:
    print("This is true")
else:
    print("This is false")
# we learn about the for loop
for i in range(5):
    print(i)
# we learn about the while loop
count = 0
while count < 5:
    print(count)
    count += 1
# we learn about the list   
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

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

#logical operator not and or 

temp = int(input("what is the temprature outside :"))

if not(temp >= 0 and temp <= 30):
    print("the temperature is good today")
    print("go outside")

elif not(temp < 0 or temp > 30):
    print("The temperature is bad today:")
    print("Stay inside!")