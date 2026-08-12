# import math
#
# print(math.e)
# print(math.pi)

"""------------------------------------------------------"""

# import math as m
#
# print(m.e)
# print(m.pi)

"""------------------------------------------------------"""

# from math import e                  #not recommended that much
# from math import pi
#
# print(e)
# print(pi)

"""---------------- Making Modules ----------------------"""

dc = 6767.67        #darkeii const.
                    # we will use these all functions in another file.... by importing "import Modules"
pie = 3.141592653589793

def square(a):
    return pow(a, 2)

def addition(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

def subtraction(*numbers):
    result = 0
    for num in numbers:
        result -= num
    return result

def factorial(a):
    result = 1
    for num in range(1, a+1):
        result *= num
    return result

def circumference(r):
    import math
    return 2 * math.pi * r

def area(r):
    import math
    return 2 * math.pi * pow(r, 2)


print(help("modules"))








