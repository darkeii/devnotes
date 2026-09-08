# Python reading files (.txt , .json, .csv)

# file_path = "stuff/input.txt"
#
# try:
#     with open(file_path, "r") as file:              # "as file": = the open() function returns an object.. which we are naming as a file here.
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("No such file found")
# except PermissionError:
#     print("You do not have permission to read that file")

# --------------------------------------------------------------------------------

# import json
#
# file_path = "stuff/input.json"
#
# try:
#     with open(file_path, "r") as file:              # "as file": = the open() function returns an object.. which we are naming as a file here.
#         content = json.load(file)
#         print(content)
#         print(content["name"])
# except FileNotFoundError:
#     print("No such file found")
# except PermissionError:
#     print("You do not have permission to read that file")

# -------------------------------------------------------------------------------

import csv

file_path = "stuff/input.csv"

try:
    with open(file_path, "r") as file:              # "as file": = the open() function returns an object.. which we are naming as a file here.
        content = csv.reader(file)
        for line in content:
            print(line)

        print()
        print(line[0])
        print(line[1])
        print(line[2])
except FileNotFoundError:
    print("No such file found")
except PermissionError:
    print("You do not have permission to read that file")





