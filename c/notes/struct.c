#include <stdio.h>
#include <stdbool.h>

// struct Student {
//     char name[50];
//     int age;
//     float gpa;
//     bool isFullTime;
// };

typedef struct {                    // using typedef .. we wont have to type struct again while defining the variable
    char name[50];                  //                  inside the main function.
    int age;
    float gpa;
    bool isFullTime;
}Student;

int main() {

    Student student1 = {
        "Darkeii",
        30,
        2.5,
        true
    };

    Student student2 = {
        "someone",
        21,
        8.9,
        false
    };

    printf("%s\n", student1.name);
    printf("%d\n", student1.age);
    printf("%.2f\n", student1.gpa);
    printf("student: %s\n", (student1.isFullTime)?"true":"false");

    printf("\n\n");

    printf("%s\n", student2.name);
    printf("%d\n", student2.age);
    printf("%.2f\n", student2.gpa);
    printf("student: %s\n", (student2.isFullTime)?"true":"false");
    
    return 0;
}
