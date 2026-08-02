# collection = single "Variable" used to store multiple valuess
#  List = [] ordered and changable, Duplicates OK
#  set = {} unordered and immutable, but Add/Remove OK , NO duplicates
#  Tuple = () ordered and unchangable, Duplicates OK, FASTER

fruits = ["apple", "banana", "orange", "coconut"]

# print(fruits[::2])
#
# for fruit in fruits:
#     print(fruit)

print(len(fruits))              #counts no. of items in list
print("apple" in fruits)        #checks if the item is in the item (boolean)

# fruits[0] = "pineapple"         #using an index we can reassign a value
# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")      #adds an item to the end of list
# fruits.remove("apple")          #removes the item
# fruits.insert(0, "pineapple")       #inserts the item at the provided index
# fruits.sort()                       #sorts alphabetically
# fruits.reverse()                    #reverses the list
# fruits.clear()                    #clears the list
# fruits.index("apple")            #gives the index of the listed item (int value)
# fruits.count("banana")          #counts the number of times the item appeared



print(fruits)






# print(dir(fruits))
# help(fruits)