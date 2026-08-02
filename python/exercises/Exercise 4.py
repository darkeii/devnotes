#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)


print("----------YOUR CART----------")

for food in foods:
    if foods.index(food) == len(foods)-1:
        print(food)
        print()
    else:
        print(food, end="    ")

for price in prices:
    total += price
    if prices.index(price) == len(prices)-1:
        print(price)
        print()
    else:
        print(price, end="    ")

print(f"Your total is {total}")
