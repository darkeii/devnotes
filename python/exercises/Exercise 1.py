#Calculating the length of the hypotenuse of a right angled triangle

import math

base = float(input("base of triangle(cm): "))
perpendicular = float(input("perpendicular of triangle(cm): "))

hypotenuse = math.sqrt(pow(base,2) + pow(perpendicular, 2))
print(f"The Hypotenuse is: {round(hypotenuse,2)}cm")



