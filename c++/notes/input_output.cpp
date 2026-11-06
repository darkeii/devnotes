#include <iostream>
#include <string>

int main() {

     // int age {19};
     // std::cout << "Age : " << age << std::endl;

     std::cerr  << "Error message : something went wrong" << std::endl;
     std::clog  << "Log message : this is a log message" << std::endl;

     //

     // std::string name;
     // int age1;
     //
     // std::cout << "Please enter your name : ";
     // std::cin >> name;
     //
     // std::cout << "Please enter your age : ";
     // std::cin >> age1;
     //
     // std::cout << "Hello " << name << ", You are " << age1 << " years old." << std::endl;

     // string with spaces

     std::string full_name;
     int age2;

     std::cout << "Please enter your name : ";
     std::getline(std::cin, full_name);

     std::cout << "Please enter your age : ";
     std::cin >> age2;

     std::cout << "Hello "
               << full_name
               << ", You are "
               << age2
               << " years old."
               << std::endl;

     return 0;
}