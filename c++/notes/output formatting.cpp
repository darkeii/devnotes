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

    std::cout << std::boolalpha;
    std::cout << true << std::endl;
    std::cout << std::noboolalpha;          // disables "boolalpha"
    std::cout << false << std::endl;

    std::cout << std::showpos;
    std::cout << +14 << std::endl;      // enables to show "+" symbol infront of positive numbers
    std::cout << std::noshowpos;
    std::cout << +18 << std::endl;      // disables "showpos"

    std::cout << "\n\n" << std::endl;

    // output in different number systems:
    // std::dec, std::hex, std::oct     // will only take effect for integral data types.

    int pos_int{717171};
    int neg_int{-4283};
    double double_var{124.989};

    std::cout << std::uppercase;        // capitalises those letters which are used to represent a number.
    //default (dec)
    std::cout << "Default format (dec)" << std::endl;
    std::cout << "pos_int : " << pos_int << std::endl;
    std::cout << "neg_int : " << neg_int << std::endl;
    std::cout << "double_var : " << double_var << std::endl << std::endl;

    //std::hex (hexadecimal)
    std::cout << std::hex;
    std::cout << "Hexadecimal" << std::endl;
    std::cout << "pos_int : " << pos_int << std::endl;
    std::cout << "neg_int : " << neg_int << std::endl;
    std::cout << "double_var : " << double_var << std::endl << std::endl;

    //std::oct (octal)
    std::cout << std::oct;
    std::cout << "Octal" << std::endl;
    std::cout << "pos_int : " << pos_int << std::endl;
    std::cout << "neg_int : " << neg_int << std::endl;
    std::cout << "double_var : " << double_var << std::endl << std::endl;

    //default (dec)
    std::cout << std::dec;                                  // back to default (decimal)
    std::cout << "Default format (dec)" << std::endl;
    std::cout << "pos_int : " << pos_int << std::endl;
    std::cout << "neg_int : " << neg_int << std::endl;
    std::cout << "double_var : " << double_var << std::endl << std::endl;

    // output with scientific values
    int a{-45};
    long double b{156.12121746716432L};
    double c{2.34e-12};

    std::cout << std::endl;
    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;
    std::cout << "c : " << c << std::endl;

    // fixed

    std::cout << std::fixed;        // it makes the program to print decimal numbers exactly how they are...
    std::cout << std::endl;
    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;
    std::cout << std::setprecision(14) << "c : " << c << std::setprecision(6) <<std::endl;      // to see the complete number, "setprecision" needs to be used.

    // scientific

    std::cout << std::scientific;
    std::cout << std::endl;
    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;
    std::cout << "c : " << c << std::endl;

    // reset all settings back to default

    std::cout.unsetf(std::ios::scientific | std::ios::fixed);       // to reset back to default
    std::cout << std::endl;
    std::cout << "a : " << a << std::endl;
    std::cout << "b : " << b << std::endl;
    std::cout << "c : " << c << std::endl;

    // std::showbase;

    std::cout << std::endl;
    std::cout << std::showbase;
    std::cout << std::hex;
    std::cout << std::nouppercase;
    std::cout << pos_int << std::endl;
    std::cout << std::noshowbase;

    return 0;
}