#include <iostream>

int main(int argc, char **argv) {

    int a{6};
    int b{3};
    int c{8};
    int d{9};
    int e{3};
    int f{2};
    int g{5};

    int result1 = a + b * c -d/e -f + g;     // 6 + 24 -3 -2 +5
    int result2 = a/b*c +d -e +f;           // (a/b)*c
    int result3 = (a + b) * c -d/e -f + g;     // 72 -3 -2 +5

    std::cout << "result1 : " << result1 << std::endl;
    std::cout << "result2 : " << result2 << std::endl;
    std::cout << "result3 : " << result3 << std::endl;

    return 0;
}
