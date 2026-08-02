import math

print(math.pi)
print(math.e)

result = math.sqrt(100)
print(result)

x = 9.4

result = math.ceil(x)       #rounds to upper int
print(result)
result = math.floor(x)      #rounds to lower int
print(result)

#Exercise

radius = float(input("radius = "))
circumference = 2*math.pi*radius
print(math.ceil(circumference))
print(math.floor(circumference))
print(round(circumference, 2))      #rounds the number upto 2 decimal places

#Exercise 2

radius = float(input("radius = "))

area = math.pi * pow(radius,2)
print(round(area, 2))