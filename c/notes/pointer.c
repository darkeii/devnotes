#include <stdio.h>

void birthday(int *age);

int main() {

    // pointer = A variable that stores the memory address of another variable.
    //          Benefit: They help avoid wasting memory by allowing you to pass
    //                  the address of a large data structure instead of copying the entire data.

    int age = 25;
    // printf("%p", &age);             // hexadecimal address

    int *pAge = &age;       // pointer created - storing the memory address of variable "age"
    int *hello = pAge;

    printf("%p\n", &age);
    printf("%p\n", &pAge);
    printf("%p\n\n", &hello);

    birthday(pAge);

    printf("You are %d years old", age);
    return 0;
}

void birthday(int *age) {
    (*age)++;               // (*age) = de- referencing the memory address of age.
                            //           so that it gives the value stored at pointer of age
}


