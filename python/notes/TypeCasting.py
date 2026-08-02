#TypeCasting = process of converting variable from one data type to another
#              str(), int(), float(), Bool()

name = "Darky"
age = 19
gpa = 6.7
is_student = True

x = type(name)
print(x)

print(type(age))

gpa = int(gpa)
print(gpa)

age = str(age)
print(type(age))

age += "1"
print(age)

name = bool(name)
print(name)

#bool() gives true even if a single character is written down

name = ""
name = bool(name)
print(name)

