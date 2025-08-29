# for loops = execute a block of code a number of times 

for i in range(1,10): # if want tto reversed
    print(i)

print("Happy new year")

credit_card = "2342-2342-2342"

for x in credit_card:
    print(x, end = " ")


for y in range (1,21):
    if y == 13:
       continue # continue or break
    else:
        print(y)