# exception = An event that interrupts the flow of a program 
#  (zeroDivisionError, ValueError, KeyError, etc.)
# 10/0
# print("Hello")
# print("Bye")
#  we try and except block is user to finally

try:
    number = int(input("Enter a number: "))
    print(10/number)
except ZeroDivisionError:
    print("You can'tDivided by zero")
except ValueError:
    print("Invalid input")
except Exception:
    print("Something went wrong")
finally:
    print("This will always execute")

print("Bye")
