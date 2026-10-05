#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    // ROCK PAPER SCISSOR game

    char *elements[] = {"rock", "paper", "scissor"};
    int num = 0;
    int best_of = 0;
    char user_input = '\0';

    printf("number of rounds: ");
    scanf("%d", &best_of);

    for (int i = 0; i < best_of; i++) {
        srand(time(NULL));
        num = rand() % 3;

        printf("r: rock, p: paper, s: scissor = ");
        scanf(" %c", &user_input);

        printf("%s\n", elements[num]);

        if ((user_input == 'r' && num == 0) || (user_input == 'p' && num == 1) || (user_input == 's' && num == 2)) {
            printf("Draw !\n");
            continue;
        }
        else if ((user_input == 'r' && num == 1) || (user_input == 'p' && num == 2) || (user_input == 's' && num == 0)) {
            printf("You lose !\n");
        }
        else {
            printf("You win !\n");
        }
    }



    return 0;
}