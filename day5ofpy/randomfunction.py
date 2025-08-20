# random psuedo
# import random

import random

x = random.randint(1,6)
y = random.random()

Mylist = ['rock', 'paper', 'scissors']
z = random.choice(Mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)

print(z)