#include <stdio.h>

int main() {
    // READ A FILE

    FILE *pFile = fopen("file handling/temp/1.txt", "r");

    char buffer[1024] = {0};

    if (pFile == NULL) {
        printf("There was an error opening the file !");
    }

    while (fgets(buffer, sizeof(buffer), pFile) != NULL) {
        printf("%s", buffer);
    }

    fclose(pFile);

    return 0;
}
