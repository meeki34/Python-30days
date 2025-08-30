# nested loop = A loop within another loop (outer, inner
# for loop, while loop) outerloop:
#   innerloop:              inner lop:

# ex: while x > 0:
#      while y > 0:
#          print("do something") 


""" for x in range(3)
    for y in range(3):
        print("do something")"""

"""while x > 0:
     for y in range(9):
        print("do something")
     x -= 1"""

# for x in range(71):
#     for y in range(1, 10):
#          print(y, end =",")
#     print()# create a new line 
    
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of colums: "))
symbol = input("Enter the symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()# this print new line 

# Pattern 1 rectangle

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()# this print new line 


# question 2

r = 5 #many row that many star

for i in range(1, r+1): # loop which is the number of row 
    for j in range(1 , i+1): # loop which is the number of star in each row
        print(1, end=" ")
    print()# this print new line 

n = 5 #many row that many star

for i in range(n, 0, -1):  
    for j in range(i):  
        print("*", end=" ")
    print()# this print new line 


