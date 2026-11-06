#include <iostream>

int main(int argc, char *argv[]) {

    // NUMBER SYSTEM

    // decimal
    int decimal = 15;

    // hexadecimal
    int hexadecimal = 0xF;

    // binary
    int binary = 0b00001111;        // it is written in this way because, 15 is stored in a 8-bit block ( 1 byte )

    // octal
    int octal = 017;

    std::cout << decimal << std::endl;
    std::cout << hexadecimal << std::endl;
    std::cout << binary << std::endl;
    std::cout << octal << std::endl;

    return 0;
}