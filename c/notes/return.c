#include <stdio.h>
#include <stdbool.h>

bool isAdult(int age) {

    if (age >= 18) {
        return true;
    }
    else {
        return false;
    }
}

int getmax(int num1, int num2) {
    if (num1 >= num2) {
        return num1;
    }
    else {
        return num2;
    }

}

double cube(double num) {
    return num * num * num;
}

double square(double num) {
    return num * num;
}


int main() {

    // int x = 2 * 2;
    // int y = 3 * 3;
    // int z = 4 * 4;
    //
    // printf("%d\n", x);
    // printf("%d\n", y);
    // printf("%d\n", z);

    double x = square(2.4);              // square(2) = 4
    double y = square(3.2);              // square(3) = 9
    double z = square(4.7);              // square(4) = 16

    double a = cube(2.4);              // cube(2) = 8
    double b = cube(3.2);              // cube(3) = 27
    double c = cube(4.7);              // cube(4) = 64

    printf("%lf\n", x);
    printf("%lf\n", y);
    printf("%lf\n\n", z);

    printf("%lf\n", a);
    printf("%lf\n", b);
    printf("%lf\n\n", c);

    int age = 0;

    printf("age: ");
    scanf("%d", &age);


    if (isAdult(age)) {
        printf("You are an Adult");
    }
    else {
        printf("You are a Minor");
    }

    int num1 = 12;
    int num2 = 108;

    printf("\n\nmax number is: %d", getmax(num1, num2));

    return 0;
}