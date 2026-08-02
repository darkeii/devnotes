#2D list is a list made up of lists

fruits =     ["apple",   "banana",  "orange",  "coconut"]
vegetables = ["celery",  "carrots", "potatoes"          ]
meats =      ["chicken", "fish",    "turkey"            ]

groceries = [fruits, vegetables, meats]         # 2d list

for item in groceries:
    print(item)

#like an Excel sheet: [rows] [column]

print(groceries[1][0])

#using nested loops here:

for item in groceries:
    for item2 in item:
        print(item2, end= "  ")
    print()