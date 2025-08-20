# exception = events that occur during the execution of a program that disrupts the normal flow of the program's instructions.
# exception handling =  act of handling an exception
# try except = used to handle exceptions

# try:
#     name = input("Enter your name")
#     if name:
#         print("This is not vaild name")
#     else:
#         print("this vaild name")    
# except Exception:
#     print("Something went wrong")

# pass

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by :'))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero: idiot")

except ValueError as e:
    print(e)
    print("Enter only Number please")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")

# today we learn about the fromatmethod, kwargs , randomfunction.expectionhandle 
# i have try to learn with my now example and i want to try more of those 
# Bro code video are very easy to understand