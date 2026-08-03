# number_guessing_game

import random

from zope.interface.common.interfaces import IValueError

number = random.randint(1,100)          #number to guess

round_num = 0

while True:
    try:
        user_input = int(input("Enter your guess: "))
        if user_input < 1 or user_input > 100:
            print("Only between (1,100)")
        elif user_input > number:
            round_num += 1
            print("high")
        elif user_input < number:
            print("low")
            round_num += 1
        else:
            round_num += 1
            print()
            print(f"Guessed in {round_num}")
            print(number)
            break
    except ValueError:
        print("Invalid")





