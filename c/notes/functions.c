#include <stdio.h>
#include <string.h>

void this_is_function(char name_is[], int age_is) {
    printf("Hello\n");
    printf("Happy Birthday %s\n", name_is);
    printf("You are %d years old", age_is);
}

int main() {

    char name[50] = "";
    int age = 0;

    printf("Enter your full name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0';

    printf("Enter your age: ");
    scanf("%d", &age);

    this_is_function(name, age);

    return 0;
}
