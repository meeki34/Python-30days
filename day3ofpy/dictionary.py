# dictonary = A changeable, unordered collection of unqiue key: value pairs
#fast because they use hashing , allow use to access a value quickly

capitals = {'usa':'washington DC',
            'India':'New dehli',
            'China':'benijing',
            'Russia':'Mosocow'
            }
print(capitals['usa'])
print(capitals.get('China'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({
 'Japan':'tokyo'
})
capitals.pop('China')
capitals.clear()
for key,value in capitals.items():
    print(key,value ,end =" ,")


#day3 of learn python where cover the base list and dictionary , set tuple, while
