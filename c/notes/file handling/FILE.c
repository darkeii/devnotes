#include <stdio.h>

int main() {

    // write a file

    FILE *pFile = fopen("temp/output.txt", "w");     // if just in case , we are not able to open the file
                                                                // then *pFile = NULL (this will happen) { NULL = address = 0 }

    char text[100] = "\0";


    if (pFile == NULL) {                                        // this is to check if file opens without any error.
        printf("Error in opening file !");
        return 1;
    }

    // since the file opened correctly.
    // now we will write something into the file.

    printf("Enter text to write: ");
    fgets(text, sizeof(text), stdin);

    fprintf(pFile, "%s", text);

    printf("File was written successfully\n");

    fclose(pFile);

    return 0;
}