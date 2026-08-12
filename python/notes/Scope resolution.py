# variable scope = where a variable is visible and accesible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in    (priority order)

"""-----------------------------------------------------------------------"""

# def func1():                #functions cant see inside other functions.
#     b = 1
#     print(a)
#
# def func2():
#     a = 2
#     print(b)

"""-----------------------------------------------------------------------"""

# def func1():                #functions cant see inside other functions.
#     x = 1
#
#     def func2():
#         # x = 2              #this local x (variable) will be used first... then enclosed one in upper function
#         print(x)
#     func2()
# func1()

""""-----------------------------------------------------------------------"""

# def func1():                #functions cant see inside other functions.
#     print(x)
#
# def func2():
#     print(x)
#
# x = 3                           #This is global variable

""""-----------------------------------------------------------------------"""

# built-in variables are ... example: importing pi from maths module etc. (last priority)


func1()
func2()



