#include <iostream>

int main(int argc, char** argv) {

    int value = 5;

    std::cout << "Value is (increasing) " << value++ << std::endl;
    std::cout << "Value is           :  " << value << std::endl;        // value = 6

    // reset value to 5

    value = 5;

    std::cout << "Value is (decreasing) " << value-- << std::endl;
    std::cout << "Value is           :  " << value << std::endl;        // value = 4

    value++;
    value++;
    value++;

    // value incremented 3 times by 1... therefore, value = 4 + 3 = 7

    std::cout << "Value is           :  " << value << std::endl;

    return 0;
}