#Hangman game
import random
from words import basic_words

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
    print(f"Answer: {answer}")

def main():
    answer = random.choice(basic_words)
    is_playing = True
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()              #created an empty set (no duplicates allowed)

    while is_playing:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input(": ").lower()


        if guess.isalpha() and len(guess) == 1:
            if guess in answer:
                guessed_letter.add(guess)
                if guess in guessed_letter:
                    print("You already guessed this letter")

                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess.upper()

            else:
                wrong_guesses += 1

        else:
            print("Invalid")
            continue

        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            is_playing = False
            print("You Won")
        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            print("You Lost")
            print("----------------------------")
            display_answer(answer)
            is_playing = False






if __name__ == '__main__':
    main()
