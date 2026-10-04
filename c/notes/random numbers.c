#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    // pseudo-random = Appear random but are determined by a mathematical formula that uses a seed value
    //                  to generate a predictable sequence of numbers.
    //                  advanced: Mersenne Twister or /dev/random

    // printf("%d", rand());       // the random number is being generated via the seed value... if seed value is same ... generated random number will be same

    srand(time(NULL));          // now the seed is changing with time (seconds) ... hence the random number generated is also changing with time.

    printf("%d\n\n", rand());      // if we run program fast.. shift + f10 twice a second ..
                                     // the random generated number wont change for that second bcz time is same (in seconds)

    printf("%d\n\n", RAND_MAX);         // will show the max value that it will generate.

    int min = 50;
    int max = 100;

    int randomNUM = (rand() % (max - min + 1)) + min;       // now the random numbers are between min, max range
    printf("%d", randomNUM);

    return 0;
}