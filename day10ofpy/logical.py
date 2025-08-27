# logically operators = evaluate multiple conditions (and, or, not)
#                       or = at least one condition is true
#                       and = both conditions are true
#                       not = reverse the result, returns false if the result is true(not false , not true) 

temp = 23
is_raining = False
is_sunny = True

if temp >= 20 and temp <= 0 and is_raining == False:
    print("It's a nice day")
    if is_sunny:
        print("Go out and enjoy the sun")
    else:
        print("Take a rain coat")
else:
    print("It's too cold or too hot")
print("Done")