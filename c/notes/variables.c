#include <stdio.h>
#include <stdbool.h>

int main() {

    /*
        4 Data types:
        1. int : intger = int var
        2. float : decimal = float var
        3.

     */


    int age = 25;
    int year = 2026;
    int quantity = 1;

    float cgpa = 8.9;           // float can store upto 6-7 after decimal characters .. to store more... use "double"
    float weight = 15.78;
    float temp = 29.4;

    double pi = 3.14159265358798;
    double e = 2.7182818284590;

    char grade = 'A';           // in char value single quote is only used here.
    char symbol = '!';          // in C we dont have string datatype... string = sequence of characters (word/ mssg). therefore we store it like this below.
    char name[] = "Darkeii";
    char food[] = "Pizza";
    char email[] = "mail@darkeii.dev";

    bool isOnline = true;           // true = 1, false = 0
    bool isStudent = true;

    printf("You are %d years old\n", age);
    printf("The year is %d \n", year);
    printf("You have ordered %d pizza\n\n", quantity);

    printf("Your cgpa is %d\n", cgpa);
    printf("Your weight is %d\n", weight);
    printf("temperature is %d\n\n", temp);

    printf("pi : %.15lf\n", pi);
    printf("e: %.15lf\n", e);

    printf("Your grade is %c\n", grade);
    printf("Your fav symbol is %c\n\n", symbol);

    printf("Hello %s\n", name);         // we use %s for a array or character stored in a char variable.
    printf("Hello %s your favorite food is %s\n", name, food);
    printf("mail me at %s\n\n", email);

    printf("%d\n\n", isOnline);

    if(isStudent){
        printf("%s is a student.\n", name);
    }
    else{
        printf("%s is not a Student.\n", name);
    }

    return 0;
}
