# scope = THe region that a variable is recogined 
# A variable is only availabe  from inside the region it is created
# A Global and locally scoped versions of a variable can be created

name = "syed zahid"

def display_name():
    name = "Code"# it only avaiable to inside this function 
    # they also know as local 
    print(name)

# global scope can be (avaiable inside and outside function)
display_name()
print(name)

"""

L = Local
E = Enclosing
G = Global 
B = Built-in


"""