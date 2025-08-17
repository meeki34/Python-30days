#while loop is an statment that will execute it;s block of code, as long a sit
#  is condition 
# remain true
name = ""

while len(name) == 0:
    name = input('Enter your name:')

print("hello " + name)

name1 = None

while not name1:
    name1 = input('Enter your name:')

print("hello " + name1)
