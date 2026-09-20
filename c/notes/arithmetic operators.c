#include <stdio.h>

int main(){

    // arithmetic operators : +  -  *  /  %  ++  --

    // int x = 2;
    // float y = 3;
    // float z = 0;

    int x = 10;
    int y = 3;
    int z = 0;


    // z = x + y;
    // z = x * y;
    // z = x / y;          // here we are diving by an integer... if our result(z) will be a float value... it cant be stored inside int z variable . therefore it will simply give 0 as output.
                        // so to prevent this... we use the denominator number and storing variable(z) as float value
    // z = x % y;
    // x++;                // adds 1 to the value of x
    // x--;                   // subtracts 1 to the value of x

    printf("%d", x);

    return 0;
}
