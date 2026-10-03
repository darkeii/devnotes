#include <stdio.h>

// int result = 0;         // GLOBAL SCOPE (hard to debug) (bad practice)
                        // it is usually only recommended for constants values

int add(int x, int y) {
    int result = x + y;
    return result;
}


int main() {

    // variables cannot share same name under same scope
    // scope = a function

    // int a = 9;
    // int a = 12;          // will give error

    int result = add(3, 4);                 // here we defined int result variable again in main function... and it works fine
                                                // bcz both the int result variable are in different scope (function).

    printf("sum: %d", result);

    return 0;
}