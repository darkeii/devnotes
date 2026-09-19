#include <stdio.h>

int main() {

    //format specifiers = Special tokens that begin with a % symbol, followed by a character that specifies the data type and optional modifiers (width, precision, flags).
    // they control how data is displayed or interpreted.

    int age = 19;
    float price = 29.99;
    double pi = 3.141592356159;
    char currency = '$';
    char name[] = "Darkeii";

    printf("%d\n", age);
    printf("%f\n", price);
    printf("%lf\n", pi);                 // can also use "%f" for double but when taking input from user we'll have to use "%lf".. so for consistency we will use %lf.
    printf("%c\n", currency);
    printf("%s\n\n", name);

    // formatting output

    int a = 1;
    int b = 10;
    int c = 100;

    printf("%10d\n", a);          // any number written between % and d = that number of spaces
    printf("%-10d\n", a);         // "-" minus sign to align the text left.
    printf("%04d\n", b);              // typing 0 before the number between % and d = minimum that number of characters will be displayed... extra characters: 0
    printf("%+d\n\n", c);             // "+" between % and d = shows that number with its respective sign .. plus or minus.

    float d = 20.11;
    float e = 67.67;
    float f = -32.45;
                                  // by default C shows upto 6 decimal places.
    printf("%.2f\n", d);              // will only show upto 2 decimal places now.
    printf("%.1f\n", e);              // output will be rounded off... if "%.(num)" num < the number of decimal places you typed.
    printf("%+7.2f\n", f);            // minimum 7 characters will be displayed, "+"  sign will show if the number is positive or negative... .2 will show decimals places till 2


    return 0;
}
