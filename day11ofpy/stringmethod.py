# string method and how to use them 

name = input("Enter your name: ")

print(len(name))
result = name.upper()
print(result)

result = name.find("syed") # find the index of the string
print(result)

result = name.capitalize()
print(result)
# or just assign a variable and print it

print(help(str)) # to see all the string methods