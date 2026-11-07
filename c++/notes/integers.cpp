#include <iostream>

int main() {

    // Braced initializers
    // Variable may contain random garbage value. WARNING

    int elephant_count;

    int lion_count{}; //Initializes to 0
    int dog_count{10}; //Initializes to 10
    int cat_count{15}; //Initializes to 15

    // Can use expression as initializer
    int domesticated_animals { dog_count + cat_count };     // Assignment initializers

    //
    // int new_number{doesnt_exist};        // will give error, because "doesnt_exist" variable doesnt exist

    // int narrow_conversion1{2.9};            // will give error bcz we are using braced initialization, therefor implicit conversion of data wont happen.
    int narrow_conversion2 = 2.9;

    // std::cout << narrow_conversion1 << std::endl;
    std::cout << narrow_conversion2 << std::endl;

    int apple_count(5);
    int orange_count(5);
    int fruit_count( apple_count + orange_count );

    int narrow_conversion_funtional (2.9);

    std::cout << "Apple Count : " << apple_count << std::endl;
    std::cout << "Orange Count : " << orange_count << std::endl;
    std::cout << "Fruit Count : " << fruit_count << std::endl;
    std::cout << "Narrowing conversion : " << narrow_conversion_funtional << std::endl << std::endl;

    std::cout << "size of int : " << sizeof(int) << std::endl;
    std::cout << "size of bool : " << sizeof(bool) << std::endl;
    std::cout << "size of long : " << sizeof(long) << std::endl;
    std::cout << "size of float : " << sizeof(float) << std::endl;
    std::cout << "size of double : " << sizeof(double) << std::endl;
    std::cout << "size of char : " << sizeof(char) << std::endl;


    return 0;
}