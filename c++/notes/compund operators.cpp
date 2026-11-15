#include <iostream>

int main(int argc, char** argv) {

    int value{45};

    value += 5;
    std::cout << value << std::endl;
    value = 45;

    value -= 5;
    std::cout << value << std::endl;
    value = 45;

    value *= 5;
    std::cout << value << std::endl;
    value = 45;

    value /= 5;
    std::cout << value << std::endl;
    value = 45;

    value %= 11;
    std::cout << value << std::endl;
    value = 45;

    return 0;
}