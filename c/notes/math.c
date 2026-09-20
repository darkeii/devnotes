#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {

    float x = 3.56;
    float y = -3;
    float z = 2.718282;
    float r = 0.0f;

    // r = sqrt(x);         //square root
    // r = pow(x, 4);
    // r = round(x);           // rounds off to the closest

    // r = ceil(x);                // rounds off to the bigger integer
    // r = floor(x);                // rounds off to the smaller integer

    // r = abs(y);                 // gives the distance from the 0.
    // r = log(z);
    // r = sin(x);
    // r = cos(x);
    r = tan(z);

    // printf("%f", x);
    printf("%f", r);

    return 0;
}

