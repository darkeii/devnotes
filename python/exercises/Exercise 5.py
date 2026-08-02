# Python Quiz game
from curses.ascii import isdigit, isalpha

from numpy.ma.core import append

questions = (("What comes after alphabet 'f' ?"),
             ("What is capital of india?"),
             ("What is color of good apple?"),
             ("What code editor are you using?"),
             ("What is your favorite game?"))

options = (("A. G","B. P","C. L","D. K"),
           ("A. Mumbai","B. Delhi","C. Kolkata","D. Lucknow"),
           ("A. orange","B. yellow","C. blue","D. red"),
           ("A. VS code","B. neoVIM","C. Pycharm","D. zed"),
           ("A. Terraria","B. Elden Ring","C. Valorant","D. CS2"))


answers = (("A"),
           ("B"),
           ("D"),
           ("C"),
           ("B"))
guesses = []
score = 0
question_num = 0

print("Welcome to the quiz !")
print()

for question in questions:
    print("-----------------------------------------------")
    print(f"{question_num+1}. {question}")
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("--> ")
        if not guess.strip():
            print("Invalid")
        elif len(guess) > 1 or isdigit(guess):
            print("Invalid")
        elif isalpha(guess):
            question_num += 1
            guesses.append(guess)
            break
        else:
            print("Invalid")

x = 0
#calculating score
for i in answers:
    if i == guesses[x]:
        score += 1
    else:
        continue
    x += 1

print("-------------------------------------------")
print(f"Your Final score is: {score}")




