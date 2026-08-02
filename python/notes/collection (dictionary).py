# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA": "washington D.C",
            "India": "Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))                  #gives the value of that key

# if capitals.get("Japan"):
#     print("capital exists")
# else:
#     print("capital doesnt exists")              #if a key:value pair doesnt exist it will return "None"


# capitals.update({"Germany": "Berlin",
#                  "USA": "Detroit"})             #adds new key:value to dictionary or overites the existing one


# capitals.pop("China")                           #removes the specific key
# capitals.popitem()                              #removes the last item of the dictionary
# capitals.clear()                                #erases the dictionary

# keys = capitals.keys()                            #lists all the keys inside the dictionary
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()                        #lists all the values inside the dictionary
# for value in capitals.values():
#     print(value)


# print(capitals.items())                           #ressembles a 2d list

"""example"""

# for item in capitals.items():
#     for x in item:
#         print(x, end= " ")
#     print()

# for item in capitals.items():
#     print(item)

"""important example"""

# for key, value in capitals.items():
#     print(f"{key}  {value}")



