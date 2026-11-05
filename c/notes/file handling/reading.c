#include <stdio.h>

int main() {

    // READ a file

    FILE *pFile = fopen("temp/input.txt", "r");
    char buffer[1024] = {0};                   // going to temporarily store data

    if (pFile == NULL) {
        printf("Could not open the file\n");
        return 1;
    }

    while (fgets(buffer, sizeof(buffer), pFile) != NULL) {

        printf("%s", buffer);

    }





    fclose(pFile);

    return 0;
}