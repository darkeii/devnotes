#Tuples = ordered , so indexing will work.... add/ remove wont work... bcz they are unchangable
from itertools import count

fruits = ("apple", "banana", "orange", "coconut", "coconut")

#print(dir(fruits))

print(fruits[2])
print(len(fruits))
print(fruits.count("coconut"))