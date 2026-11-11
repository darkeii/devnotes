#include <iostream>

int main(int argc, char **argv) {

    int variable1 = 55;     // variable is initialized
    std::cout << variable1 << std::endl;

    variable1 = 20;         // initialized variable's value is changed.
    std::cout << variable1 << std::endl;

    // when updating values of "auto" initialized varaibles, we need to be careful.

    auto num{32ul};
    std::cout << sizeof(num) << std::endl;
    std::cout << num << std::endl;

    num = -50;      // DANGER !, the "num" varaible we initilized was an unsigned variable,
                    // but now we are putting "-ve" value in it. == it will give garbage number.

    std::cout << sizeof(num) << std::endl;
    std::cout << num << std::endl;

    return 0;
}