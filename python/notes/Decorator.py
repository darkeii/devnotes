# Decorator = A function that extends the behaviour of another function
#              w/o modifying the base function
#               Pass the base function as an argument to the decorator
#
#
#               @add_sprinkles
#               get_ice_cream("vanilla")
#

def add_sprinkles(func):                # This is the format you neeed to follow to apply decorators to the base function.
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You added fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):               # to give some input in these commands we use *args, **kwargs in the parameters of wrapper function so that it can take any amount of values
    print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla")


