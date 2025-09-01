# Array is a collection of data of same type 
# we using list in python 

# fruits =["apple","banana","mango","grapes","orange"]
# vegetable = ["potato","tomato","carrot","brinjal","onion"]
# meats = ["chicken","fish","mutton","lamb","beef"]

# groceries = [fruits , vegetable , meats]
# # print(groceries[1][2])

# print(groceries[0][1][3])

groceries = [("apple","banana","mango","grapes","orange"),("potato","tomato","carrot","brinjal","onion"),("chicken","fish","mutton","lamb","beef")]

for collection in groceries:
    for food in collection:
        print(food, end=" ")   
    print()