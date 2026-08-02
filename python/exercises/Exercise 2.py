# simple calculator

import math

num1 = int(input("enter 1st number: "))
operator = input("ENter your operation (+,-,/,*,root): ")
num2 = int(input("enter your 2nd number: "))

if operator == "+": #addition
    print(f"result = {num1 + num2}")
elif operator == "-": #subtraction
    print(f"result = {num1 - num2}")
elif operator == "/":   #division
    print(f"result = {num1/num2}")
elif operator == "*":      #multipy
    print(f"result = {num1*num2}")
elif operator == "root":
    print(f"sqrt of 1st number = {math.sqrt(num1)}")
    print(f"sqrt of 2nd number = {math.sqrt(num2)}")
else:
    print("Invalid operator")