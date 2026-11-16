#include <iostream>
#include <ostream>
#include <istream>
#include <iomanip>

int main(int argc, char** argv) {
    // std::flush       // from "ostream" lib.

    std::cout << "Hello world" << std::flush;
    std::cout << "Hello world" << std::flush;       // It flushes the output from buffer memory to the terminal (user can see)

    std::cout << "Hello world" << std::endl;        // std::endl = std::flush + \n
    std::cout << std::endl;

    // std::setw()      // from "iomanip" lib.
    int n{15};
    std::cout << std::setfill('#');
    std::cout << std::setw(n + 8) << "Formatted Table" << std::endl;

    std::cout << std::left;

    std::cout << std::setw(n) << "First" << std::setw(n) << "Last" << std::setw(n) << "age" << std::endl;
    std::cout << std::setw(n) << "Shubhanshu" << std::setw(n) << "Maurya"  << std::setw(n) << 19 << std::endl;
    std::cout << std::setw(n) << "Aryan" << std::setw(n) << "Singh" << std::setw(n) << 18 << std::endl;
    std::cout << std::setw(n) << "Josh" << std::setw(n) << "Mosh" << std::setw(n) << "42" << std::endl;

    // center align is a bit complex for now... = you will have to subtract the length of string from the total width. then divide the remaining spaces by 2
    // Or easier : You can use std::format and its " ^ " to center align
    std::cout << "\n-----------------------------------------------------------------------------------\n" << std::endl;

    std::cout << std::right;
    std::cout << std::setw(n + 8) << "Formatted Table" << std::endl;
    std::cout << std::left;

    // std::cout << std::internal;

    std::cout << std::setw(n) << "Numbers" <<  std::setw(n) << "Value" << std::endl;
    std::cout << std::setw(n) << "number 1" <<  std::setw(n) << -31 << std::endl;
    std::cout << std::setw(n) << "number 2" <<  std::setw(n) << 24 << std::endl;
    std::cout << std::setw(n) << "number 3" <<  std::setw(n) << -81 << std::endl;
    std::cout << "\n" << std::endl;


    return 0;
}