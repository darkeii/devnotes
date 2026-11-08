#include <iostream>

int main(int argc, char **argv) {

    unsigned int value1 {2147483649};       // Can only store +ve values... threrefore its range is reserved for only +ve integers.
    // signed int value2 {2147483649};         // can store both -ve and +ve value...
                                            // therefore its range gets divided equally in the negative part and postive part of integers

    std::cout << value1 << std::endl;
    // std::cout << value2 << std::endl;

    long long int A{0};
    short unsigned int B{0};
    long unsigned int C{0};
    long signed int D{0};
    signed int E{0};

    std::cout << sizeof(A) << std::endl;
    std::cout << sizeof(B) << std::endl;
    std::cout << sizeof(C) << std::endl;
    std::cout << sizeof(D) << std::endl;
    std::cout << sizeof(E) << std::endl;

    return 0;
}