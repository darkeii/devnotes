#include <iostream>

int main() {

    // AND : &&
    // OR  : ||
    // NOT : !

    std::cout << std::boolalpha;

    bool a{false};
    bool b{true};
    bool c{true};

    std::cout << (!(a && b) || c) << std::endl;         // (a && b) = false

    return 0;
}