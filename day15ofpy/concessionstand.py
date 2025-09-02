# concession stand program

menu = {
    "popcorn": 5.50,
    "candy": 2.50,
    "coke": 3.00,
    "soda": 3.00,
    "water": 2.00
}

cart = []
total = 0

print("--------- MENU ---------")
for key,  value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("------------------------")
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("--------- CART ---------")
for food in cart:
    total  += menu.get(food)
    print(food, end = " ")


print()
print(f"Total: ${total:.2f}")