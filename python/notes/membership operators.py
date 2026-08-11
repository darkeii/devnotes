# membership operators = used to test whether a value or variable is found in a sequence
#                           (string, list, tuple, set , dictionary)
#                     1. in
                    # 2. not in

# word = "apple"
#
# letter = input("Guess a letter in the secret word: ")
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found !")|


# students = {"suresh", "mahesh", "ramesh"}
#
# student = input("name of student: ")
# if student not in students:
#     print("Not in list")
# else:
#     print(f"{student} is in list")


# grades = {
#     "sandy": "A",
#     "ramesh": "B",
#     "patrick": "C",
#     "suresh": "A+"
# }
#
# student = input("name of student: ").lower()
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found !")


email = input("email: ")

if "@" in email and "." in email:
    print(f"{email} is valid")
else:
    print(f"{email} is not an valid email")
