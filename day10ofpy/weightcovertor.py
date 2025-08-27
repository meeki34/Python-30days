# python covertor from kg to pounds

weight = float (input("Enter weight :"))
unit = input("Kilograms or Pounds (K or L) : ")

if unit == "K":
    weight = weight * 2.20462
    unit = "Lbs."
    print(f"Weight in Lbs :{round(weight)} {unit} ")

elif unit == "L":
    weight = weight / 2.20462
    unit = "Kgs."
    print(f"Weight in Kg :{round(weight)} {unit} ")
else:
    print("Invalid unit")

# You're input is {unit}, is not valid unit
