#Hangman game
import random

words = ("apple", "orange", "banana", "coconut", "pineapple", "grapes", "berry")

# dictionary of key():
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        " | ",
        "/  "),
    4: (" O ",
        " | ",
        "/ \\"),
    5: (" O ",
        "/| ",
        "/ \\"),
    6: (" O ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("***************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************************")
    print()

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint = []
    for x in answer:
        hint.append("_")
    wrong_guesses = 0
    guessed_letters = set()              #to make an empty set(tuple), we have to use set() method.
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        print()
        print(answer)

        guess = input(": ").lower()

        if guess.isalpha():
            for letter in guess:
                try:
                    index = answer.index(letter)
                    guessed_letters.add(answer[index])
                except ValueError:
                    continue

            print(guessed_letters)
            display_hint(hint)
        else:
            print("Invalid !")

if __name__ == '__main__':
    main()
