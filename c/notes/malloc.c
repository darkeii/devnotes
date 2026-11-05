#include <stdio.h>
#include <stdlib.h>

int main() {
    // malloc() = A function in C that dynamicaally allocates
                    // a specified number of bytes in memory.

    // char grades[5] = {0};

    int number = 0;
    printf("Enter the number of grades: ");
    scanf("%d", &number);

    char *grades = malloc(number * sizeof(char));       // using this malloc function is like renting free space for our work.

    if (grades == NULL) {
        printf("memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < number; i++) {
        printf("Enter grade #%d: ", i+ 1);
        scanf(" %c", &grades[i]);
    }

    for (int i = 0; i < number; i++) {
        printf("%c ", grades[i]);
    }
                                                        // after our work is done we need to free this used space by us.
    free(grades);           // returning the rented space back to the OS.
    grades = NULL;          // avoids dangling pointers.

    return 0;
}
