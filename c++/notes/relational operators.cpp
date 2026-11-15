#include <iostream>

int main() {

    int num1{45};
    int num2{60};

    std::cout << "number 1 : " << num1 << std::endl;
    std::cout << "number 2 : " << num2 << std::endl;

    std::cout << std::boolalpha;

    // Need to use parenthesis here:

    std::cout << "number 1 < number 2 : " << (num1 < num2) << std::endl;        // will give boolean value
    std::cout << "number 1 > number 2 : " << (num1 > num2) << std::endl;
    std::cout << "number 1 <= number 2 : " << (num1 <= num2) << std::endl;
    std::cout << "number 1 >= number 2 : " << (num1 >= num2) << std::endl;
    std::cout << "number 1 == number 2 : " << (num1 == num2) << std::endl;
    std::cout << "number 1 != number 2 : " << (num1 != num2) << std::endl;

    return 0;
}