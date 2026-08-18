#Banking Program


def show_balance(balance):
    print(f"Your balance: ${balance:.2f}")

def deposit():
    amount = float(input("Amount to be deposited: $"))
    if amount <= 0:
        print(f"${amount} is not valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    withdraw_amount = float(input("Amount to be withdrawn: $"))
    if withdraw_amount <= 0:
        print(f"${withdraw_amount} is not valid amount")
        return 0
    elif withdraw_amount > balance:
        print("Insuficient amount")
        return 0
    else:
        return withdraw_amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print()
        print("Banking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print()

        choice = input("> ").lower()
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("Invalid")


    print("Thank You!")

if __name__ == '__main__':
    main()


