# Concession stand program

menu = {"pizza": 3,                        #---------------------------------
        "nachos": 4.5,                       #---------------------------------
        "burger": 5,                       #----- Dictionary ----------------
        "soda": 6.5,                         #---------------------------------
        "cola": 4                          #---------------------------------
}

cart = []
total = 0

print("------------MENU----------------")
for key, value in menu.items():
    print(f"- {key:10} -     ${value:.2f}")
print("---------------------------------")

while True:
    food = input("Select an item (q to quit): ")
    food = food.lower()
    if food == "q":
        break
    else:
        if menu.get(food) is not None:
            cart.append(food)
        else:
            print("item not in menu")



for item in cart:
    if menu.get(item):
        total += menu.get(item)


print("---------------------------------")
print(f"Your total: {total}")


