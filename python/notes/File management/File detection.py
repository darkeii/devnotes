# Python file detection

import os  # os = operating system

# file_path = "stuff/test.txt"              # This path is called relative path.. when the target file is next to the code file.
file_path = "/home/shubhanshum/Projects/devnotes/python/notes/File management/stuff"      #(directory)      # This path is called Absolute path.

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That doesnt exists.")




