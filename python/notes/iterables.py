# literables = An object/collection that can return its elements one at a time,
#                 allowing it to be iterated over in a loop.

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

for num in reversed(numbers):
    print(num, end=" - ")

fruits = {"apple", "banana", "orange", "guava"}

for fruit in fruits:             #reversed function can be applied for sets
    print(fruit)

"""tuple, list, sets ---- all are iterable"""

name = "darkeii"
for character in name:
    print(character, end="'")

dictionary = {"A": 1,
              "B": 2,
              "C": 3,
              "D": 4}

for a, b in dictionary.items():
    print(a)
    print(b)