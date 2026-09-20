#include <stdio.h>
#include <string.h>

int main(){

    int age = 0;
    float gpa = 0.0f;
    char grade = '\0';
    char name[30] = "";

    printf("Enter Your age: ");
    scanf("%d", &age);

    printf("Enter your gpa: ");
    scanf("%f", &gpa);

    printf("Enter your grade: ");
    // scanf("%c", &grade);                // it didnt give us opportunity to type in the grade.. because it took the \n character as its input... to ignore that new line character (\n)
                                        // we will put a space before the "%" = " %c" (exactly like this) this tells the program to ignore the new line character
    scanf(" %c", &grade);

    getchar();
    printf("Enter your full name: ");
    // scanf("%s", &name);                 // scanf stop reading the input after any white spaces.
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0';      // from the <string.h> library. this will replace the last character with null character ( replace \n character with emptiness )

    printf("%d\n", age);
    printf("%.2f\n", gpa);
    printf("%c\n", grade);
    printf("%s\n", name);



    return 0;
}
