#include <stdio.h>
#include <stdbool.h>

int main() {
    int num = 0;

    printf("Please enter a number: ");
    scanf("%d", &num);

    for (int i = 2; i <= num; i++) {
        bool is_prime = true;

        for (int divisor = 2; divisor * divisor <= i; divisor++) {
            if (i % divisor == 0) {
                is_prime = false;
                break;
            }
        }

        if (is_prime) {
            printf("%d\n", i);
        }
    }

    return 0;
}