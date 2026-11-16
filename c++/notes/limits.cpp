#include <iostream>
#include <limits>

int main() {

    // std::numeric_limits<T>::min() = gives the minimum possible +ve number.
    // std::numeric_limits<T>::max() = gives the maximum possible +ve number.
    // std::numeric_limits<T>::lowest() = gives the minimum possible negative number.

    std::cout << "The range of the short is from: " << std::numeric_limits<short>::lowest() << std::endl;       // lowest = min
    std::cout << "The range of the short is from: " << std::numeric_limits<short>::min() << std::endl;





    return 0;
}