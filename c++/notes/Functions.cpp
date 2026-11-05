#include <iostream>

int add(int a, int b);

int main(int argc, char **argv) {

    std::cout << "sum : " << add(31, 49) << std::endl;

    return 0;
}

int add(int a, int b) {
    return a + b;
}
