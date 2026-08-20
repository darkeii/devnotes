#Slot machine

import random
import time

def spin_row():
    symbols = ["🍒", "🍑", "🍌", "🍊", "🍇"]

    return [random.choice(symbols) for _ in range(3)]               # "_" is used to tell... for every iteration (specially in list comprehension lists)

def print_row(row):
    print("|".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        print("***********************")
        print("Jackpot x100")
        print("***********************")
        return bet*100

    elif row[0] == row[1] or row[1] == row[2] or row[2] == row[0]:
        return bet*10
    return 0

def main():

    balance = 100           #starting money
    balance_set = {100}

    print("***************************")
    print("Welcome to the python slots")
    print("***************************")
    print()

    while balance > 0:
        print(f"Current balance: ${balance}")
        balance_set.add(balance)

        bet = input("bet: ")

        if bet.isdigit():
            bet = int(bet)
            if bet <= 0 or bet > balance:
                print("Please enter valid amount")
            else:
                balance -= bet
                print("spinning", end="")

                for seconds in range(3):
                    time.sleep(0.67)
                    print(".", end= "")

                spin_row()
                row = spin_row()
                print_row(row)

                balance += get_payout(row, bet)

                print()
        elif bet == "exit":
            balance = 0
            print("Thanks for playing !")
        else:
            print("Invalid !")

    print()
    print(f"Your Max Balance: ${max(balance_set)}")





if __name__ == '__main__':
    main()


