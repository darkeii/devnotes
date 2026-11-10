#include <iostream>

int main(int argc, char **argv) {

    char value1 = 20;       // assigning a decimal number to a char type .. assigns it as a ASCII code...
    char value2 = 65;       // char 65 == A

    int v1 = 30;
    int v2 = 50;


    std::cout << value2 << std::endl;
    std::cout << value1 + value2 << std::endl;
    std::cout << sizeof(value1 + value2) << std::endl;

    std::cout << v1 + v2 << std::endl;
    std::cout << sizeof(v1 + v2) << std::endl;

    if (value2 == 'A') {
        std::cout << "yes" << std::endl;
    }

    std::cout << "-----------------------------------------" << std::endl;

    // static_cast

    std::cout << static_cast<int>(value2) << std::endl;
    std::cout << sizeof(value2) << std::endl;                       // value2 = char
    std::cout << sizeof(static_cast<int>(value2)) << std::endl;     // value2 = int

    return 0;
}