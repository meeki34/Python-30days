# create an calculator using if statments

operator = input("Enter operator (+ - * /) :")
num1 = float(input("Enter 1st number :"))
num2 = float(input("Enter 2nd number :"))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
     result = num1 - num2
     print(round(result, 3))
elif operator == "*":
     result = num1 * num2
     print(round(result, 3))
elif operator == "/":
     result = num1 / num2
     print(round(result, 3))
else:
    print("You're input is {operator}, is not valid operator")

