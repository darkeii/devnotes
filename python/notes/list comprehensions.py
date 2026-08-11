# list comprehension = A concise way to create lists in python
#                         compact and easier to read than traditional loops
#           format    =   [expression for value in iterable if condition]

doubles = []
for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

"""to make the above code simpler and easier to read we use list comprehension"""

# triples = [expression for value in iterable if condition]

triples = {x * 3 for x in range(1,11) if x % 2 ==0}
print(triples)

squares = [pow(x, 2) for x in range(1,11)]
print(squares)

fruits = ["apple", "banana", "orange", "watermelon"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

"""-----------------------------------------------------------------------------------------"""

numbers = [3, 1, -4, 6, -9, 2, -2]
positive_num = [x for x in numbers if x > 0]
negative_num = [x for x in numbers if x < 0]
even_num = [x for x in numbers if x % 2 == 0]
odd_num = [x for x in numbers if x not in even_num]

print(positive_num)
print(negative_num)
print(even_num)
print(odd_num)