#include <stdio.h>
// #include <windows.h>        // for windows only
#include <unistd.h>         // for linux/mac only

int multiplication_table();

int main() {

    // for loop = repeat some code a limited number of times
    //             for(Initialization ; condition ; update)

    for (int i = 3; i >= 1; i--) {
        // Sleep(1000);             // windows   (milliseconds)
        sleep(1);            // Linux/ Mac  (seconds)
        printf("%d\n", i);
    }

    multiplication_table();

    return 0;
}

    // break = leaves the loop completely.. breaks out of the loop
    // continue = skips the current loop cycle

int multiplication_table() {

    for (int i = 1; i <= 10; i++) {
        for (int j = 1; j <= 10; j++) {
            printf("%3d ", i * j);
        }
        printf("\n");
    }
}