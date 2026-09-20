#include <stdio.h>

int main() {

    // SHOPPING CART PROGRAM

    char item[50] = "";
    float price = 0.0f;
    int quantity = 0;
    char currerncy = '$';
    float total = 0.0f;

    printf("What item would you like to buy?: ");
    scanf("%s", &item);


    printf("What is the price for each item?: ");
    scanf("%f", &price);              // precision modifiers cant work with scanf (.2)

    printf("How many would you like?: ");
    scanf("%d", &quantity);

    total = price * quantity;

    printf("\nYou have bought %d %s for %c%.2f each\n", quantity, item, currerncy, price);
    printf("Your total is: %c%.2f", currerncy, total);


    return 0;
}
