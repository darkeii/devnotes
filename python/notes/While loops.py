
name = input("Enter your name: ")

while name == "":
    print("please enter your name")

print(f"Hello {name}")

food = input("Enter your favorite food ('q' to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter your favorite food ('q' to quit): ")

print("bye")


num = int(input("Enter a num between 1 - 10: "))

while num < 1 or num > 10:
    print((f"{num} is not valid"))
    num = int(input("Enter a num between 1 - 10: "))

print(f"Your number is {num}")

