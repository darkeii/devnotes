
# Object = a bundle of related attributes (variables) and methods (functions)
#             Eg: phone, cup , book
#               You need a class to create many objects

# Class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Buggati", 2022, "black", False)
car3 = Car("Charger", 2017, "Blue", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print("*******************************")

car3.drive()
car1.stop()

car2.describe()

