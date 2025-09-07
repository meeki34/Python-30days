# Decorator = A function that extends the behavior of another function 
#            w/o modifying the base function 
#              Pass the base function as an argument to the decorator function 
#              The decorator function returns a new function that wraps the \
#              base function with additional functionality
#              Ex : @add_sprinkles
#                   def make_cake():
#                      print("make a cake")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):# wrapper function is the new function that wraps the base function
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("chocolate")