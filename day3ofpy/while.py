#Loop Control statment = change a loops execution from its normal sequence

# break 
# continue 
# pass

#break come out of the loop and the program
while True:
    name = input("Enter ur name")
    if name != "":
        break

#continue move to next statement and print that

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end ="")

# pass is skip the statment and move to next statment 
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)