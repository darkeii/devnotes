#include <stdio.h>
#include <stdbool.h>

// void hello(char name[], int age) {
//     printf("Hello %s\n", name);
//     printf("You are %d years old\n", age);
// }

void hello(char name[], int age);       // function prototype
bool ageCheck(int age);

int main() {

    //function prototypes = Provide the compiler w/ information about a function's:
                            // name, return type, and parameters before its actual definition.
                            // Enables type checking and allows functions to be used before they're defined'
                            // Imporves readability, organization, and helps prevent errors.

    int age = 0;
    printf("age: ");
    scanf("%d", &age);

    hello("Darkeii", age);

    if (ageCheck(age)) {
        printf("You are an Adult");
    }

    return 0;
}

void hello(char name[], int age) {
    printf("Hello %s\n", name);
    printf("You are %d years old\n", age);
}

bool ageCheck(int age) {
    if (age >= 18) {
        return true;
    }
    else {
        return false;
    }
}