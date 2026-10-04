#include <endian.h>
#include <stdio.h>

int main() {

    int rows = 0;
    int columns = 0;
    char symbol = '\0';

    printf("Enter number of rows: ");
    scanf("%d", &rows);

    printf("Enter number of columns: ");
    scanf("%d", &columns);

    printf("char to print: ");
    scanf(" %c", &symbol);

    printf("\n");

    for (int row = 1; row <= rows; row++) {
        for (int column = 1; column <= columns; column++) {
            printf("%c ", symbol);
        }
        printf("\n");
    }


    return 0;
}