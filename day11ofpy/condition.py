# condition = A oneline shotcut for if statement (ternary operator)
# formal for this oneline  X if condition else Y
# print or Assign a value based on the condition
# print("Positive" if num > 0 else "Negative")
num = 6
a = 18
b = 20
temperature = 25

permission = "Guest"
# print("Positive"if num > 0 else "Negative")

# result = "Even" if num % 2 == 0 else "Odd"
# max_value = a if a > b else b 
# min_value = a if a < b else b 
# status = "Adult" if a >= 18 else "Minor"
# weather = "hotweather" if temperature > 30 else "Cold"
access = "Full Access" if permission == "Admin" else "Limited Access"
print(access)