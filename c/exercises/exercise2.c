#include <stdio.h>
#include <string.h>

int main() {

    // MAD LIBS GAME

    char noun[50] = "";
    char verb[50] = "";
    char adj1[50] = "";
    char adj2[50] = "";
    char adj3[50] = "";

    printf("Enter an adjective (description): ");
    scanf("%s", &adj1);

    printf("Enter a noun (animal or person): ");
    scanf("%s", &noun);

    printf("Enter an adjective (description): ");
    scanf("%s", &adj2);

    printf("Enter a verb (ending w- ing): ");
    scanf("%s", &verb);

    printf("Enter an adjective (description): ");
    scanf("%s", &adj3);


    printf("\n\nToday we went to a %s zoo.\n", adj1);
    printf("In an exhibit, I saw a %s.\n", noun);
    printf("%s was %s and %s !\n", noun, adj2, verb);
    printf("I was %s!\n", adj3);
    return 0;
}
