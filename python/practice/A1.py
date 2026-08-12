# 1. Custom PC Build Analyzer
# Create a program to manage a high-end PC parts list.
#
#     Use a dictionary where the keys are part names (e.g., "CPU", "GPU") and values are their prices in INR.
#
#     Write a function that calculates the total cost.
#
#     Use a list comprehension to create a new list containing only the names of parts that cost more than 50,000 INR.
#
#     Print the final filtered list and the total cost using format specifiers for two decimal places.

CPU = {
    "i5": 25000,
    "i7": 45000,
    "i9": 70000
}

GPU = {
    "gtx 1650": 16000,
    "rtx 3050": 20000,
    "rtx 4090": 68000,
    "rtx 5090": 140000
}

RAM = {
    "8": 4500,
    "16": 9000,
    "32": 17000
}

MONITOR ={
    "asus": 13999.99,
    "lenovo": 15999.99,
    "acer": 19999.99,
    "samsung": 22999.99
}

pc_parts = [CPU, GPU, RAM, MONITOR]
cart = {}
total = 0

for parts in pc_parts:
    if "i5" in parts:
        print("-------- CPU -----------")
    elif "GTX 1650" in parts:
        print("-------- GPU -----------")
    elif "8" in parts:
        print("-------- RAM -----------")
    elif "Asus" in parts:
        print("------ MONITOR ---------")

    for key, price in parts.items():
        print(f"{key:10}: {price:,.2f}")
    print("------------------------")

    while True:
        user_input = input("> ").lower()
        if user_input in parts:
            cart.update({key: price})
            break
        else:
            print("Invalid")
            continue

    print()


print("-------- Your cart -----------")
for key, price in cart.items():
    print(f"{key:10}  -----> {price:,.2f}")
    total += price

print()
print(f"Your total is : ${total:,.2f}")






