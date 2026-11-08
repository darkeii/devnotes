#include <iostream>
#include <iomanip>

int main() {

    // fractional numbers also use a number system ... = IEE_754

    float A {1.234567890123f};                  // precise till 8
    double B {1.2345678901234567890};           // precise till 16
    long double C {1.2345678901234567890L};     // precise till 18

    std::cout << std::setprecision(20);     // by default C++ only displays upto 6 decimal.. using this library and this funtion
                                                  // we can increase the precision.

    std::cout << A << std::endl;
    std::cout << B << std::endl;
    std::cout << C << std::endl;
    std::cout << -4.98/0 << std::endl;             // a float/double number can be divided by 0 = giving +inf if +ve and -inf if -ve.
    std::cout << 0.0/0.0 << std::endl;             // when float/double number is : 0/0 --> gives -nan

    double number1{0.000000002345};

    std::cout << number1 << std::endl;



    return 0;
}