# kwargs = parameter that will pack all arguments into a dicitonary
# useful so that a function can accept a varying amount of keyword arguments


"""def hello(first, last):
    print("Hello" + first + " " + last)


hello(first= "Bro",last="syed")"""

def hello(**name):
   # print("hello" + kwargs ['first'] + " " + kwargs ['last'])
   print('hello', end = " ")
   for key,value in name.items():
      print(value, end =" ")


hello(first= "Mr.",middle='Syed',last="zahid")