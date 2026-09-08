# Python writing files (.txt, .json , .csv)

txt_data = "This is a .txt file"

file_path = "stuff/output.txt"

# try:                                                    # w : write file
#     with open(file_path, "w") as file:                  # x : writes file, but gives error if file alrdy exists "FileExistsError"
#         file.write("\n" + txt_data)                     # a : append
#         print(f"txt file {file_path} was created")      # r : read file
#
# except FileExistsError:
#     print("This file already exists")

# ------------------------------------------------------------------------------------------------
#
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
#
# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#
#         print(f"txt file {file_path} was created")
#
# except FileExistsError:
#     print("This file already exists")

# ------------------------------------------------------------------------------------------------

# writing .json files

# import json
#
# employee = {
#     "name" : "Spongebob",
#     "age" : 30,
#     "job" : "cook"
# }
#
# file_path = "stuff/test.json"
#
# with open(file_path, "w") as file:
#     json.dump(employee, file, indent= 4)               # dump() makes the dictionary in json variable form.
#     print("Json file was created")
#
# ------------------------------------------------------------------------------------------------

# writing csv file

import csv              # CSV is like spreadsheet/xml data

employees = [["Name", "Age", "Job"],        # 2D list, list of lists (rows and columns)
             ["Spongebob", 30, "Cook"],
             ["Sandy", 27, "Scientist"],
             ["Patrick", 37, "Unemployed"]]

file_path = "stuff/test.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"csv file was created")




