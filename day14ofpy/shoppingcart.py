# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy:(q to quit) :  ")
    if food.lower() == "q":
        break
    else: 
        price = input(f"Enter the price of {food}: ₹")
        quantity = input(f"How many {food} do you want to buy?  ")

        foods.append(food)
        prices.append(price)
        print("Item added to cart!")
    

print("======== YOUR CART ======")

for food in foods:
    print(food, end = " ")

for price in prices:
    total += float(price)

for quantity in prices:
    total += float(quantity) 

print(quantity, end = " ")
print(f"\nTotal: ₹{total}")
print("Thank you for shopping with us!")

