# rock paper scissor game

import random

R = "r"                  #-----------------------------------------
P = "p"                 #--------DRY = dont repeat yourself-------
S = "s"                #-----------------------------------------

choices = (R, P, S)

game_data = {"r": "rock",
             "p": "paper",
             "s": "scissors"
}

try:
    number_of_rounds = int(input("Number of rounds you want to play: "))
except ValueError:
    print("type an integer")

score = 0

for round in range(0,number_of_rounds):
    while True:
        computer_input = random.choice(choices)
        user_input = input("(r,p,s) : ").lower()
        if user_input.isalpha() and game_data.get(user_input):
            print(game_data.get(computer_input))
            if user_input == computer_input:                                #draw condition
                print("draw")
            elif ((user_input == R and computer_input == S) or
                  (user_input == P and computer_input == R) or
                  (user_input == S and computer_input == P)):               # Win condition
                score += 1
            break

        else:
            print("Invalid !")


print("------------------------------")
if score >= number_of_rounds//2:
    print("You Won")
else:
    print("You Lost")
print("------------------------------")

