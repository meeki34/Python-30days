thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
thislist[1] = "blackcurrant"
print(thislist)
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("orange")
print(thislist)
thislist.pop()


# for loop in list 
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
print(thislist)
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
thislist.reverse()
print(thislist)
thislist.sort(key = str.lower)
print(thislist)