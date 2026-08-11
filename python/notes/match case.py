# match-ccase statement (switch) = An alternative to using many 'elif' statements
#                                     execute some code if a value matches 'case'
#                                 pros: cleaner and readable


# def day_of_weeknd(day):
#     if day == 1:
#         return "Sunday"
#     elif day == 2:                            #-----------------------------------------------------
#         return "Monday"                       #-----------------------------------------------------
#     elif day == 3:                            #----- Instead of this we can use match-case----------
#         return "Tuesday"                      #-----------------------------------------------------
#     elif day == 4:                            #-----------------------------------------------------
#         return "Wednesday"
#     elif day == 5:
#         return "Thursday"
#     elif day == 6:
#         return "Friday"
#     elif day == 7:
#         return "Saturday"
#     else:
#         return "Invalid !"
#
# print(day_of_weeknd(int(input("day: "))))

                                                             # '|' is used as = 'or'
def day_of_weeknd(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:                                  # "_" underscore is used for "else"... no matching case
            return "Invalid"

print(day_of_weeknd(int(input("day: "))))


