#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void won(int num_of_guess);

int main() {

    // Number guessing game

    srand(time(NULL));

    int min = 1;
    int max = 100;

    int number = (rand() % (max - min + 1)) + min;

    int guess_num = 0;
    int num_of_guess = 0;
    bool is_playing = true;

    while (is_playing) {
        printf("\nGuess a number: ");
        scanf("%d", &guess_num);

        if (guess_num == number) {
            won(num_of_guess);
            break;
        }
        else {

            num_of_guess++;

            if (guess_num > number) {
                printf("TOO HIGH !");
            }
            else {
                printf("TOO LOW !");
            }
        }
    }
    return 0;
}

void won(int num_of_guess) {
    printf("CORRECT !\n");
    printf("Guessed in %d chances", num_of_guess);
}
