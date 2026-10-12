#include <stdio.h>

// enum Day {
//     SUNDAY = 1, MONDAY = 2, TUESDAY = 3, WEDNESDAY = 4, THURSDAY = 5, FRIDAY = 6, SATURDAY = 7              // if we dont assign any number to them,
// };                                                                                                          // by default it assigns increasing numbers to the
//                                                                                                             // variable inside enum.
// USING ABOVE METHOD , WE WILL HAVE TO TYPE "enum Day today"

typedef enum {
    SUNDAY = 1, MONDAY = 2, TUESDAY = 3, WEDNESDAY = 4, THURSDAY = 5, FRIDAY = 6, SATURDAY = 7
}Day;

typedef enum {
    SUCCESS, FAILURE, PENDING
}Status;

// USING THE ABOVE METHOD, WE WONT HAVE TO USE "enum" again to use this data type.

void connectStatus(Status status);

int main() {

    // enum = A user-defined data type that consists of a set of named integer constants.
    // Benefit: Replaces numbers with readable names.

    // SUNDAY = 0;
    // MONDAY = 1;
    // TUESDAY = 2;

    Day today = SUNDAY;
    //
    // printf("%d", today);

    if (today == SUNDAY || today == SATURDAY) {
        printf("Its weekend !\n\n");
    }
    else {
        printf("It is a Weekday\n\n");
    }

    // -----------------------------------------------------------------------------------------------------------------

    Status status = PENDING;

    connectStatus(status);

    return 0;
}

void connectStatus(Status status) {

    switch (status) {
        case SUCCESS:
            printf("Connection was successful\n");
            break;
        case FAILURE:
            printf("Connection failed\n");
            break;
        case PENDING:
            printf("Connecting...\n");
            break;
    }
}