# return = statement used to end a funtion
#             and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def subt(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x*y
    return z

print(add(3,4))

multiply(3,4)               # after calling this function , this output is the returned value i.e, 12

print(multiply(3,4))

print("------------------------------------------------------------------------")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("gengoku", "kyojori")
print(full_name)


