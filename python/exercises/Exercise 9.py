# die roller program

import random

die_art = {
    1: ("⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬜️ ⬛️ ⬜️ ⬜️" ,
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️"),

    2: ("⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬛️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️" ,
       "⬜️ ⬜️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️"),

    3: ("⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬛️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬜️ ⬛️ ⬜️ ⬜️" ,
       "⬜️ ⬜️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️"),

    4: ("⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️" ,
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️"),

    5: ("⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬛️ ⬜️ ⬜️" ,
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️"),

    6: ("⬜️ ⬜️ ⬜️ ⬜️ ⬜️",
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️" ,
       "⬜️ ⬛️ ⬜️ ⬛️ ⬜️",
       "⬜️ ⬜️ ⬜️ ⬜️ ⬜️"),


}

dice = []
total = 0

num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    die_num = random.randint(1,6)
    dice.append(die_num)
    for row in die_art.get(die_num):
        print(row)
        print(end= " ")
    print()

print(dice)

for die in dice:
    total += die
print(f"Total: {total}")
