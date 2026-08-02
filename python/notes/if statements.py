from urllib import response

age = int(input("Enter your age: "))

if age >= 100:
    print("Too Old to sign up!")
elif age >= 18:
    print("You are now signed up")
elif age <= 0:
    print("Get Borned !!!")     #ik grammar shut up
else:
    print("You must be 18+ to sign up!")

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you")
else:
    print("Only Y/N man")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")
