# if __name__ == '__main__' : (this script can be imported OR run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#                 helps readabllity,
#                 leaves no global variables,
#                 avoid unintended execution)

#           Ex. library = import library for functionality
#                             when running library directly, display a help page

"""--------------------------------------------------------------------------------------------------------"""

print(__name__)             #If you run the script directly in your terminal, Python assigns the string '__main__' to that variable.
                            #If you import the script into a completely different file, Python assigns the script's actual file name to the variable instead.

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is main function")

if __name__ == '__main__':
    main()