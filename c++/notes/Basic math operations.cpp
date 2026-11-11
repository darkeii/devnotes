#include <iostream>

int main(int argc, char **argv) {

    // ADDITION
    auto a{6};
    auto b{10};
    auto add_result{a + b};

    // SUBTRACTION
    auto c{50};
    auto d{20};
    auto subt_result{c-d};

    // MULTIPLICATION
    auto e{10};
    auto f{2};
    auto multi_result{e * f};

    // DIVISION ( integer division )
    auto g{31};
    auto h{10};
    auto div1_result{g / h};        // The output of the following operation is an integer because, the variables that we initilized were deduced to "int" datatype by "auto"

    // DIVISION ( fractional division )
    auto i{9.0};
    auto j{2.5};
    auto div2_result{i / j};

    // MODULUS ( gives the remainder after the DIVISION )
    auto k{67};
    auto l{5};
    auto mod_result{k % l};

    std::cout << add_result << std::endl;
    std::cout << subt_result << std::endl;
    std::cout << multi_result << std::endl;
    std::cout << div1_result << std::endl;
    std::cout << div2_result << std::endl;
    std::cout << mod_result << std::endl;


    return 0;
}