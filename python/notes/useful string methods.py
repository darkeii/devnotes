
name = input("Enter your full name: ")

#result = len(name)      #counts no. of character in string including spaces
#result = name.find("h")     #finds the character position/index from start
#result = name.rfind("h")     #finds the character position/index from last
#result = name.capitalize()      #makes the 1st letter of the string capital
#result = name.upper()       #capitalises all letters in string
#result = name.lower()      #lowercases all letters in string
#result = name.isdigit()     #gives boolean value True only when all the letter in string are digits
#result = name.isalpha()     #gives boolean value True only when all the letter in string are alphabets ... not even space
#result = name.count("D")        #counts the number of that character
#result = name.replace("D", "B")     #replaces the character... can even replace with empty string to remove the character
result = name.__add__(name)


print(result)

print(help(str))
