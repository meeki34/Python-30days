# While loop = repeat a block of code while a condition is true
# it can go on forever if you don't change the condition

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num = int(input("Enter a number between 1 and 10: "))
food = input("Enter a food you like (q to quit): ")

# if name == " ":
#    print("You didn't enter anything!")
# else:
#     print(f"Hello {name}")

while name == "":
    print(" You didn't enter anything!")
    name = input("Enter your name: ")
    break
print(f"Hello {name}")

while age < 0:
   print("Age can't be negative!")
print(f"You are {age} years old")

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10:"))

print(f"You entered {num}")

while not food == 'q':
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")



