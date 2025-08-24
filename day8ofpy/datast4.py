# str.replace(old,new)

sentence = "I am learning Python"
print(sentence.replace("Python","Java"))

#Polymorphism
#Polymorphism is often used in Class methods, 
#where we can have multiple classes with the same method name.

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
        
    def language(self):
        print("Hindi is the most widely spoken language of India.")
        
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
        
    def language(self):
        print("English is the primary language of USA.")
        
    def type(self):
        print("USA is a developed country.")

# object of India class and USA class
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()