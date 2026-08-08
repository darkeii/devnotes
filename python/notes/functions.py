# funtion = A block of reusable code
#           place () after a function name of invoke it


def hbd(name,age):                                #inside () terms are called parameters
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old!")
    print("Lalalala !")

hbd("darkeii", 19)                     #while calling the functions, inside () terms are called arguments (positional arguments)
hbd("zenitsu", 20)                     #arguments fill the places of parameters.... (Order matters)


print("---------------------------------------------------------------------------------------------------------------")
print()

def display_invoice(username, amount, due_date):
    print(f"hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("darkeii", 500, "06/08/2026")