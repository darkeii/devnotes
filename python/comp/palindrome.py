#palindrone

is_palindrome = False

while True:
    user_input = input("text: ")

    if user_input.isalpha():
        for i in range(0, len(user_input) // 2):
            if user_input[i] == user_input[len(user_input) -1 - i]:
                is_palindrome = True
            else:
                is_palindrome = False
                break

        if is_palindrome:
            print("Number is palindrome")
        else:
            print("Number is not palindrome")
        break

    else:
        print("Write a text message !")

