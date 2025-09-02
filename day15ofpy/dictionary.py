#dictionary = a collection of {key:value} pairs
#ordered, changeable, no duplicates

Dict = {"City:bengalure","State:Karnataka"}

print(Dict)

print(type(Dict))

print(len(Dict))

print(Dict["City"])

print(Dict.keys())

print(Dict.values())

print(Dict.items())

Dict["City"]="Hyderabad"
print(Dict)

Dict.update({"Country":"India"})
print(Dict)

Dict.pop("State")
print(Dict)

Dict.popitem()
print(Dict)

Dict.clear()
print(Dict)

del Dict
print(Dict)

Dict = {"City:bengalure","State:Karnataka"}

Dict2 = Dict.copy()
print(Dict2)