#include <iostream>

int main(int argc, char **argv) {

    // "auto" datatype = Lets the compiler deduce the datatype

    auto var1 {12};
    auto var2 {13.0};
    auto var3 {14.0f};
    auto var4 {15.01};
    auto var5 {'e'};

    // int modifier suffixes
    auto var6 {123u};       // unsigned
    auto var7 {123ul};      // unsigned long
    auto var8 {123ll};      // long long

    std::cout << sizeof(var1) << std::endl;
    std::cout << sizeof(var2) << std::endl;
    std::cout << sizeof(var3) << std::endl;
    std::cout << sizeof(var4) << std::endl;
    std::cout << sizeof(var5) << std::endl;

    std::cout << sizeof(var6) << std::endl;
    std::cout << sizeof(var7) << std::endl;
    std::cout << sizeof(var8) << std::endl;


    return 0;
}