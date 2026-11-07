#include <iostream>

int main(int argc, char **argv) {

    std::string name;

    std::cout << "Name : ";
    std::getline(std::cin, name);


    std::cout << name << std::endl;
}