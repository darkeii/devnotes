 # *args              = allows you to pass multiple non-key arguments -----> packs the arguments in a "tuple"
 # **kwargs           = allows you to pass multiple keyword arguments ------> packs the arguments in a "dictionary"
 #                      * = unpacking operator
 #
 #                1. positional  2. default  3. keyword  4. ARBITRARY

# def add(a, b):
#     return a + b
#
# print(add(1, 2))

"""*args"""

# def add(*args):
#     sum = 0
#     print(type(args))
#     for num in args:
#         sum += num
#     return sum
#
# print(add(1, 2, 3))
# print(add(4,6,5,5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Dr. ", "spongebob", "squarepants")

"""--------------------------------------------------------------------------"""

"""**kwargs"""

# def print_address(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
#
# print_address(street= "123 street A for applpe",
#               apt = "100",
#               city= "electricity",
#               state= "flow state",
#               zip= "open/close"
#               )

"""using both *args and **kwargs"""

def shipping_label(*a, **k):
    for arg in a:
        print(arg, end=" ")
    print()
    for value in k.values():
        print(value)

shipping_label("Dr. ", "Spongebob", "Squarepants", "III",
               street = "fake street",
               city = "Mumbai",
               state = "Maharashtra",
               zip = "1234",
               country = "India"
               )








