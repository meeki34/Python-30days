# temperature covertor program

unit = input("Enter the unit you want to convert to (C or F) :")
temp = int(input("Enter the temperature : "))

if unit == "C":
    temp = round((temp - 9) / 5 + 32 , 1)
    print(f"Temperature in Fahrenheit:{temp} Fahrenheit")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"Temperature in Celsius: {temp} Celsius") 
else: 
    print("Invalid unit")