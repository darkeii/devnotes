#include <iostream>

int main() {

    bool high_traffic{false};
    bool weather_clear{true};

    std::cout << high_traffic << std::endl;
    std::cout << weather_clear << std::endl;

    std::cout << std::boolalpha;        // This forces the program to print true/false instead of 0,1 like python

    std::cout << high_traffic << std::endl;
    std::cout << weather_clear << std::endl;
    std::cout << "-----------------------------------------------------------" << std::endl;

    if (high_traffic == false) {
        if (weather_clear == true) {
            std::cout << "You CAN go Out !" << std::endl;
        }else {
            std::cout << "You CANNOT go out !" << std::endl;
        }
    }else {
        std::cout << "You CANNOT go out !" << std::endl;

    }




    return 0;
}
